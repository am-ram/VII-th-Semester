<?php
$db_host='localhost';
$db_user='root';
$db_passwd='root@123';
$db_name='votedb';
$con = mysqli_connect($db_host,$db_user,$db_passwd,$db_name)
or
die("Error connecting to the database");
?>