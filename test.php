<?php
header('Content-Type: application/json');
echo json_encode(['debug' => 'ok', 'method' => $_SERVER['REQUEST_METHOD']]);
