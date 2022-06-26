<?php

require_once './Digit.php';

// démarrage de la session
session_start();

fd_exit_session(isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '../index.php');

?>
