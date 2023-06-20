<<<<<<< HEAD
<?php 
session_start();
//檢查 session 中的 passed 變數是否等於 TRUE 
//如果 session 中的 passed 變數等於 TRUE
//表示已登入網站，將使用者導向首頁 HM.html
if (isset($_SESSION['id'])==false)
{
	//顯示訊息提醒使用者即將返回起始畫面
	echo "<script type='text/javascript'>";
	echo "alert('尚未登入，即將返回起始畫面');";
	echo "location.href='../index.html'";		
	echo "</script>";
}
//如果 session 中的 passed 變數等於 TRUE
//表示已經登入網站，取得使用者資料	
else
{
require_once("../php/dbtools.inc.php");

//建立資料連接
$link = create_connection();

//執行 SELECT 陳述式取得使用者資料
$sql = "SELECT * FROM user_status";
$result = execute_sql($link, $sql, "graduation_project");

$_SESSION['status'] = sqlsrv_fetch_object($result)->status;

    if($_SESSION['status'] == "True"){
        header("location:../html/PST_cd.php");
    }else{
        echo "<script type='text/javascript'>";
        echo "alert('尚未掃描成功，即將返回QRcord畫面');";
        echo "location.href='../html/PST.php'";
        echo "</script>";
    }
    
}
=======
<?php 
session_start();
//檢查 session 中的 passed 變數是否等於 TRUE 
//如果 session 中的 passed 變數等於 TRUE
//表示已登入網站，將使用者導向首頁 HM.html
if (isset($_SESSION['id'])==false)
{
	//顯示訊息提醒使用者即將返回起始畫面
	echo "<script type='text/javascript'>";
	echo "alert('尚未登入，即將返回起始畫面');";
	echo "location.href='../index.html'";		
	echo "</script>";
}
//如果 session 中的 passed 變數等於 TRUE
//表示已經登入網站，取得使用者資料	
else
{
require_once("../php/dbtools.inc.php");

//建立資料連接
$link = create_connection();

//執行 SELECT 陳述式取得使用者資料
$sql = "SELECT * FROM user_status";
$result = execute_sql($link, $sql, "graduation_project");

$_SESSION['status'] = sqlsrv_fetch_object($result)->status;

    if($_SESSION['status'] == "True"){
        header("location:../html/PST_cd.php");
    }else{
        echo "<script type='text/javascript'>";
        echo "alert('尚未掃描成功，即將返回QRcord畫面');";
        echo "location.href='../html/PST.php'";
        echo "</script>";
    }
    
}
>>>>>>> origin/main
?>