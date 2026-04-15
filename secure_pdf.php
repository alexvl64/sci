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

// Vérification du hash fourni — hash_equals() pour éviter les timing attacks
if ($given_hash === '' || !hash_equals($real_hash, $given_hash)) {
    http_response_code(403);
    exit("Forbidden");
}

// Headers de sécurité
header("Content-Type: application/pdf");
header("Content-Length: " . filesize($path));
header('Content-Disposition: inline; filename="' . $file . '"');
header("Cache-Control: no-store, no-cache, must-revalidate, private");
header("Pragma: no-cache");
header("X-Content-Type-Options: nosniff");
header("X-Robots-Tag: noindex, nofollow, noarchive");

readfile($path);
exit;
