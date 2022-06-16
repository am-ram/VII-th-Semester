<?php
$db_host='localhost';
$db_user='root';
$db_passwd='root@123';
$db_name='votedb';
$dbh= mysqli_connect($db_host,$db_user,$db_passwd,$db_name)
or
die("Error connecting to the database");
echo"connectionis success";
$crtdb= "CREATE DATABASE votedb";
$result=mysqli_query($dbh,$crtdb) or die("Error in query");
echo "votedbcreated";
$crttb= "CREATE TABLE login (
uidVARCHAR(13) PRIMARY KEY,
password VARCHAR(30) NOT NULL,
profile TINYINT NOT NULL,votedBOOLEAN)";
$crttb= "CREATE TABLE student (
    uidVARCHAR(13) PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    section VARCHAR(7) NOT NULL)";
    $crttb= "CREATE TABLE candidate (
    cidINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    cnameVARCHAR(30) NOT NULL,
    section VARCHAR(7) NOT NULL,
    votecountINT NULL,
    photo BLOB NULL,
    manifesto BLOB NULL)";
    $result=mysqli_query($dbh,$crttb) or die("Error in query");
    echo "table created";
    ?>