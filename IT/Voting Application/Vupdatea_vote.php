<?php
include("vconnect.php");
$name = $_POST['candidate'];
$query = "update candidate set votecount=votecount+1 where cid='$name'";
mysqli_query($con,$query) or die("Error updating the vote");
echo "Your vote is successful"."<br/>";
?>