<<<<<<< HEAD
<?php
session_start();
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");

//取得表單資料
$account = $_POST["account"];
$password = $_POST["password"];
// echo $account;
// echo $password;
//建立資料連接
$link = create_connection();
//檢查帳號密碼是否正確
$sql = "SELECT * FROM users Where account = '$account' AND password = '$password'";
$result = execute_sql($link, $sql, "graduation_project");
// echo $sql;
// $id = sqlsrv_fetch_object($result)->id;
// echo $id;
// while( $row = sqlsrv_fetch_array( $result, SQLSRV_FETCH_NUMERIC) ) {
//     echo"<tr>";
//     for($i = 0;$i<sqlsrv_num_fields($result);$i++)
//         echo "<tr>$row[$i] , </tr>";
//     echo"</tr>";
// }

// 如果帳號密碼錯誤
if (sqlsrv_has_rows($result) == 0)
{
//釋放 $result 佔用的記憶體
sqlsrv_free_stmt($result);

//關閉資料連接	
sqlsrv_close($link);
    
//顯示訊息要求使用者輸入正確的帳號密碼
echo "<script type='text/javascript'>";
echo "alert('帳號密碼錯誤，請查明後再登入');";
echo "history.back();";
echo "</script>";
}

//如果帳號密碼正確
else
{
//取得 id 欄位
// $id = sqlsrv_fetch_object($result)->id;
$_SESSION['id'] = sqlsrv_fetch_object($result)->id;
$_SESSION['passed'] = "TRUE";

$filename = $_SESSION['id'];
//資料夾的建立
$file_path = "C:/inetpub/wwwroot/video/$filename/";
if(!file_exists($file_path)){
    mkdir($file_path);
    // echo "建立資料夾成功";
// }else{
    // echo "資料夾已存在";   
}   
//釋放 $result 佔用的記憶體	
sqlsrv_free_stmt($result);   
//關閉資料連接	
sqlsrv_close($link);
//將使用者資料加入session
header("location:../html/HM.php");
}
=======
<?php
session_start();
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");

//取得表單資料
$account = $_POST["account"];
$password = $_POST["password"];
// echo $account;
// echo $password;
//建立資料連接
$link = create_connection();
//檢查帳號密碼是否正確
$sql = "SELECT * FROM users Where account = '$account' AND password = '$password'";
$result = execute_sql($link, $sql, "graduation_project");
// echo $sql;
// $id = sqlsrv_fetch_object($result)->id;
// echo $id;
// while( $row = sqlsrv_fetch_array( $result, SQLSRV_FETCH_NUMERIC) ) {
//     echo"<tr>";
//     for($i = 0;$i<sqlsrv_num_fields($result);$i++)
//         echo "<tr>$row[$i] , </tr>";
//     echo"</tr>";
// }

// 如果帳號密碼錯誤
if (sqlsrv_has_rows($result) == 0)
{
//釋放 $result 佔用的記憶體
sqlsrv_free_stmt($result);

//關閉資料連接	
sqlsrv_close($link);
    
//顯示訊息要求使用者輸入正確的帳號密碼
echo "<script type='text/javascript'>";
echo "alert('帳號密碼錯誤，請查明後再登入');";
echo "history.back();";
echo "</script>";
}

//如果帳號密碼正確
else
{
//取得 id 欄位
// $id = sqlsrv_fetch_object($result)->id;
$_SESSION['id'] = sqlsrv_fetch_object($result)->id;
$_SESSION['passed'] = "TRUE";

$filename = $_SESSION['id'];
//資料夾的建立
$file_path = "C:/inetpub/wwwroot/video/$filename/";
if(!file_exists($file_path)){
    mkdir($file_path);
    // echo "建立資料夾成功";
// }else{
    // echo "資料夾已存在";   
}   
//釋放 $result 佔用的記憶體	
sqlsrv_free_stmt($result);   
//關閉資料連接	
sqlsrv_close($link);
//將使用者資料加入session
header("location:../html/HM.php");
}
>>>>>>> origin/main
?>