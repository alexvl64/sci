<?php
error_reporting(E_ALL); // Report all errors
ini_set('display_errors', '1'); // Display errors on the screen


// L'URL cible vers laquelle les requêtes sont redirigées
$targetUrl = "https://app.sparkcore-investment.com/prospect/widget/create/hP30R4dl4427m";

// Capturer la méthode HTTP
$method = $_SERVER['REQUEST_METHOD'];

// Capturer les en-têtes
$headers = [];
foreach (getallheaders() as $key => $value) {
    $headers[] = "$key: $value";
}

// Capturer le corps de la requête (le cas échéant)
$body = file_get_contents('php://input');

// Initialiser cURL
$ch = curl_init($targetUrl);

// Définir les options de cURL
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method); // Définir la méthode HTTP (GET, POST, PUT, etc.)
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);   // Retourner la réponse au lieu de l'afficher directement
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);   // Transférer les en-têtes

if ($method !== 'GET') {
    curl_setopt($ch, CURLOPT_POSTFIELDS, $body);  // Joindre le corps de la requête pour les requêtes non GET
}

// Exécuter la requête
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

// Vérifier les erreurs cURL
if (curl_errno($ch)) {
    #http_response_code(500);
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'Erreur cURL : ' . curl_error($ch),
    ]);
    exit;
}

// Fermer cURL
curl_close($ch);

// Définir le code de statut HTTP en fonction de la réponse
#http_response_code($httpCode);

// Vérifier si la réponse est du JSON
if (json_decode($response) === null && json_last_error() !== JSON_ERROR_NONE) {
#    http_response_code(500);
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'La réponse reçue n\'est pas un JSON valide',
        'raw_response' => $response,
    ]);
    exit;
}

// Chemin vers la base de données SQLite
$dbPath = __DIR__ . '/request_limit.db';
#die('test');
// Créer la base de données et la table si elles n'existent pas
$db = new SQLite3($dbPath);
$db->exec("CREATE TABLE IF NOT EXISTS request_limits (
    ip TEXT PRIMARY KEY,
    request_count INTEGER,
    last_request_time INTEGER
)");

// Obtenir l'adresse IP du client
$ip = $_SERVER['REMOTE_ADDR'];

// Vérifier le nombre de requêtes pour cette IP
$stmt = $db->prepare("SELECT request_count, last_request_time FROM request_limits WHERE ip = :ip");
$stmt->bindValue(':ip', $ip, SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray(SQLITE3_ASSOC);

$currentTime = time();
$limitReached = false;

if ($row) {
    $requestCount = $row['request_count'];
    $lastRequestTime = $row['last_request_time'];

    // Réinitialiser le compteur si la dernière requête date de plus d'une heure
    if ($currentTime - $lastRequestTime > 3600) {
        $requestCount = 0;
    }

    if ($requestCount >= 3) {
        $limitReached = true;
    } else {
        // Incrémenter le compteur de requêtes
        $requestCount++;
        $stmt = $db->prepare("UPDATE request_limits SET request_count = :request_count, last_request_time = :last_request_time WHERE ip = :ip");
        $stmt->bindValue(':request_count', $requestCount, SQLITE3_INTEGER);
        $stmt->bindValue(':last_request_time', $currentTime, SQLITE3_INTEGER);
        $stmt->bindValue(':ip', $ip, SQLITE3_TEXT);
        $stmt->execute();
    }
} else {
    // Ajouter une nouvelle entrée pour cette IP
    $stmt = $db->prepare("INSERT INTO request_limits (ip, request_count, last_request_time) VALUES (:ip, 1, :last_request_time)");
    $stmt->bindValue(':ip', $ip, SQLITE3_TEXT);
    $stmt->bindValue(':last_request_time', $currentTime, SQLITE3_INTEGER);
    $stmt->execute();
}

if ($limitReached) {
    http_response_code(429);
    header('Content-Type: application/json');
    echo json_encode(['error' => 'Limit Reached']);
    exit;
}

// Retourner la réponse de l'URL cible
header('Content-Type: application/json'); // Supposons que la réponse est au format JSON
echo $response;
