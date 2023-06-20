<<<<<<< HEAD
<?php
session_start();
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");

//取得表單資料
// $id = $_COOKIE["id"];
$id = $_SESSION['id'];
$oldpassword = $_POST["oldpassword"]; 	
$newpassword = $_POST["newpassword"];
// echo $oldpassword;
// echo $newpassword;
//建立資料連接
$link = create_connection();

//執行 SQL 命令，更新此密碼
$sql = "UPDATE users SET password='$newpassword' WHERE id = $id";
$result = execute_sql($link, $sql, "graduation_project");
// echo $sql;
// echo $result;
// if( $result == false ) {
//   echo "0";
// }
// else{
//   echo "1";
// }

//關閉資料連接	
sqlsrv_close($link);
header("location:../html/SET.php");
=======
<?php
session_start();
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");

//取得表單資料
// $id = $_COOKIE["id"];
$id = $_SESSION['id'];
$oldpassword = $_POST["oldpassword"]; 	
$newpassword = $_POST["newpassword"];
// echo $oldpassword;
// echo $newpassword;
//建立資料連接
$link = create_connection();

//執行 SQL 命令，更新此密碼
$sql = "UPDATE users SET password='$newpassword' WHERE id = $id";
$result = execute_sql($link, $sql, "graduation_project");
// echo $sql;
// echo $result;
// if( $result == false ) {
//   echo "0";
// }
// else{
//   echo "1";
// }

//關閉資料連接	
sqlsrv_close($link);
header("location:../html/SET.php");
>>>>>>> origin/main
?>