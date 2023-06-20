<<<<<<< HEAD
<?php
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");
//建立資料連接
$link = create_connection();

$status = "False";

$sql = "UPDATE user_status SET status = '$status'";
$result = execute_sql($link, $sql, "graduation_project");


//關閉資料連接	
sqlsrv_close($link);
header("location:../html/HM.php");
=======
<?php
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");
//建立資料連接
$link = create_connection();

$status = "False";

$sql = "UPDATE user_status SET status = '$status'";
$result = execute_sql($link, $sql, "graduation_project");


//關閉資料連接	
sqlsrv_close($link);
header("location:../html/HM.php");
>>>>>>> origin/main
?>