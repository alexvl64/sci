<?php

// Paramètres
$file = basename($_GET['file'] ?? '');
$given_hash = $_GET['h'] ?? '';

// Chemin réel du fichier PDF
$path = __DIR__ . '/ressources/' . $file;

// Vérification que c’est un PDF et existe
if (!preg_match('/\.pdf$/i', $file) || !file_exists($path)) {
    http_response_code(404);
    exit("File not found");
}

// Calcul du hash SHA-256
$real_hash = hash_file('sha256', $path);

// Vérification du hash fourni
if ($given_hash === '' || $given_hash !== $real_hash) {
    http_response_code(403);
    exit("Forbidden");
}

// Envoi du PDF
header("Content-Type: application/pdf");
header("Content-Length: " . filesize($path));
readfile($path);
exit;
