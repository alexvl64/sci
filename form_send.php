<?php
// ============================================================
// form_send.php — SparkCore Investment contact form handler
// ============================================================

header('Content-Type: application/json');

// Only accept POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method Not Allowed']);
    exit;
}

// --- Honeypot check ---
$honeypot = $_POST['website'] ?? '';
if ($honeypot !== '') {
    // Silent reject — don't reveal to bots that they were caught
    echo json_encode(['status' => 'success']);
    exit;
}

// --- Rate limiting (SQLite) ---
$dbPath = __DIR__ . '/request_limit.db';
$db = new SQLite3($dbPath);
$db->exec("CREATE TABLE IF NOT EXISTS request_limits (
    ip TEXT PRIMARY KEY,
    request_count INTEGER,
    last_request_time INTEGER
)");

$ip = $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';
$currentTime = time();

$stmt = $db->prepare("SELECT request_count, last_request_time FROM request_limits WHERE ip = :ip");
$stmt->bindValue(':ip', $ip, SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray(SQLITE3_ASSOC);

if ($row) {
    $requestCount = $row['request_count'];
    $lastRequestTime = $row['last_request_time'];

    // Reset counter if last request was over 1 hour ago
    if ($currentTime - $lastRequestTime > 3600) {
        $requestCount = 0;
    }

    if ($requestCount >= 3) {
        http_response_code(429);
        echo json_encode(['error' => 'Limit Reached']);
        exit;
    }

    $requestCount++;
    $stmt = $db->prepare("UPDATE request_limits SET request_count = :rc, last_request_time = :lrt WHERE ip = :ip");
    $stmt->bindValue(':rc', $requestCount, SQLITE3_INTEGER);
    $stmt->bindValue(':lrt', $currentTime, SQLITE3_INTEGER);
    $stmt->bindValue(':ip', $ip, SQLITE3_TEXT);
    $stmt->execute();
} else {
    $stmt = $db->prepare("INSERT INTO request_limits (ip, request_count, last_request_time) VALUES (:ip, 1, :lrt)");
    $stmt->bindValue(':ip', $ip, SQLITE3_TEXT);
    $stmt->bindValue(':lrt', $currentTime, SQLITE3_INTEGER);
    $stmt->execute();
}

// --- Cloudflare Turnstile verification ---
require_once __DIR__ . '/form_config.php';

$token = $_POST['cf-turnstile-response'] ?? '';
if (!$token) {
    http_response_code(400);
    echo json_encode(['error' => 'Missing Turnstile token']);
    exit;
}

$ch = curl_init('https://challenges.cloudflare.com/turnstile/v0/siteverify');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
    'secret'   => TURNSTILE_SECRET_KEY,
    'response' => $token,
    'remoteip' => $ip,
]));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
$verifyRaw = curl_exec($ch);
$verifyErr = curl_errno($ch);
curl_close($ch);

if ($verifyErr || !$verifyRaw) {
    http_response_code(502);
    echo json_encode(['error' => 'Turnstile verification unavailable']);
    exit;
}

$verify = json_decode($verifyRaw, true);
if (!$verify || empty($verify['success'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Turnstile verification failed']);
    exit;
}

// --- Forward to Formcarry ---
$ch = curl_init('https://formcarry.com/s/oHdZL-AalnM');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
    'prenom'          => $_POST['prenom'] ?? '',
    'nom'             => $_POST['nom'] ?? '',
    'telephone'       => $_POST['telephone'] ?? 'Non renseigné',
    'email'           => $_POST['email'] ?? '',
    'source'          => $_POST['source'] ?? '',
    'source_tracking' => $_POST['source_tracking'] ?? '',
]));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 15);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept: application/json']);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlErr  = curl_errno($ch);
curl_close($ch);

if ($curlErr || !$response) {
    http_response_code(502);
    echo json_encode(['error' => 'Network error']);
    exit;
}

http_response_code($httpCode);
echo $response;
