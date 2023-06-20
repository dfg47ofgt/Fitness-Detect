<<<<<<< HEAD
<?php
session_start(); 

//在session_start();底下才能使用$_SESSION

unset($_SESSION['id']);   //將「指定」的session清除
unset($_SESSION['passed']);   //將「指定」的session清除

session_destroy();      	   //清除使用中的session
echo "<script type='text/javascript'>";
echo "alert('已登出，即將返回起始畫面');";
echo "location.href='../index.html'";		
echo "</script>";
=======
<?php
session_start(); 

//在session_start();底下才能使用$_SESSION

unset($_SESSION['id']);   //將「指定」的session清除
unset($_SESSION['passed']);   //將「指定」的session清除

session_destroy();      	   //清除使用中的session
echo "<script type='text/javascript'>";
echo "alert('已登出，即將返回起始畫面');";
echo "location.href='../index.html'";		
echo "</script>";
>>>>>>> origin/main
?>