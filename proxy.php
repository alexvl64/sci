<?php
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
    http_response_code(500);
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'Erreur cURL : ' . curl_error($ch),
    ]);
    exit;
}

// Fermer cURL
curl_close($ch);

// Définir le code de statut HTTP en fonction de la réponse
http_response_code($httpCode);

// Vérifier si la réponse est du JSON
if (json_decode($response) === null && json_last_error() !== JSON_ERROR_NONE) {
    http_response_code(500);
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'La réponse reçue n\'est pas un JSON valide',
        'raw_response' => $response,
    ]);
    exit;
}

// Retourner la réponse de l'URL cible
header('Content-Type: application/json'); // Supposons que la réponse est au format JSON
echo $response;
?>
