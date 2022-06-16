<?php
include("vconnect.php");
SESSION_START();
$query = "select * from candidate “;
$result = mysqli_query($con,$query) or die("Error querying the database");
$S=$_SESSION['user'];
$qwe="update login set voted=1 where uid='$S'";
mysqli_query($con,$qwe);
echo '<form id="myform" action="update_vote.php" method="POST">';
while($row = mysqli_fetch_array($result))
{
    echo '<input type="radio" id="name1" name="candidate"
    value="'. $row['cid']. '">'. $row['cname']. '</input><br/>';
}
echo '<input type="submit" value="vote">';
echo '</form>';
?>