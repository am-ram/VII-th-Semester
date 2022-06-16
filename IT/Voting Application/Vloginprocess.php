<?php
SESSION_START();
include("vconnect.php");
If ($con==false) echo "connection error".mysqli_connect_error($con);
If($_SERVER["REQUEST_METHOD"]=="POST")
{
$username=$_POST['uname'];
$pass=$_POST['pwd'];
$_SESSION['user']=$username;
$sql= "SELECT * FROM login where uid='$username'";
if ($res = mysqli_query($con, $sql))
{
if (mysqli_num_rows($res) > 0)
{
    while ($row = mysqli_fetch_array($res))
    {
        if($row['password']!=$pass)
        {
        echo"passwordis not matching";
        }
        else
        {if($row['profile']==0)
        {header('location:vadmin.php');
        }if(($row['profile']==1) && ($row['voted']==0))
        { header('location:vvote.html');
        }else
        {
        echo "you are alredayvoted.. Thank You!";
        }
        if(($row['profile']==2)&& ($row['voted']==0))
        {header('location:vcandidate.php');
        }
        if(($row['profile']==2)&& ($row['voted']!=0))
        {header('location:vresult.php');
        }
        }
        }
        }else {echo"wronguser name";
        }
    } else echo"querycan't execute"; mysqli_free_result($res);
}
    ?>