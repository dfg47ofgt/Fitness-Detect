<<<<<<< HEAD
<?php
session_start();
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");

$id = $_SESSION['id'];
$lift = $_POST["lift"]; 
$squat = $_POST["squat"]; 
$pushup = $_POST["pushup"];

if(isset($_POST['weeklyexercise1'])){
    $Monday = "true";
}else{
    $Monday = "false";
}
if(isset($_POST['weeklyexercise2'])){
    $Tuesday = "true";
}else{
    $Tuesday = "false";
}
if(isset($_POST['weeklyexercis3'])){
    $Wednesday = "true";
}else{
    $Wednesday = "false";
}
if(isset($_POST['weeklyexercise4'])){
    $Thursday = "true";
}else{
    $Thursday = "false";
}
if(isset($_POST['weeklyexercise5'])){
    $Friday = "true";
}else{
    $Friday = "false";
}
if(isset($_POST['weeklyexercise6'])){
    $Saturday = "true";
}else{
    $Saturday = "false";
}
if(isset($_POST['weeklyexercise7'])){
    $Sunday = "true";
}else{
    $Sunday = "false";
}
$link = create_connection();

//執行 UPDATE 陳述式來更新使用者資料
$sql = "SELECT * FROM user_goal Where goalID = '$id'";
$result = execute_sql($link, $sql, "graduation_project");
$row = sqlsrv_fetch_array($result, SQLSRV_FETCH_NUMERIC); 
if (sqlsrv_has_rows($result) != 0){

    //釋放 $result 佔用的記憶體
    sqlsrv_free_stmt($result);

    //執行 UPDATE 陳述式來更新使用者資料
    $sql = "UPDATE user_goal SET Monday = '$Monday', Tuesday = '$Tuesday', Wednesday = '$Wednesday', Thursday = '$Thursday', 
    Friday = '$Friday', Saturday = '$Saturday', Sunday = '$Sunday', 
    goalSport1 = '$lift', goalSport2 = '$squat', goalSport3 = '$pushup' WHERE  goalID = '$id'";
    $result = execute_sql($link, $sql, "graduation_project");
    // if( $result == false ) {
    //     echo "0";
    // }
    // else{
    //     echo "1";
    //     echo "更新成功";
    // }
}
else{
    //釋放 $result 佔用的記憶體
    sqlsrv_free_stmt($result);

    //執行 SQL 命令，新增此健身次數
    $sql = "INSERT INTO user_goal (goalID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, 
    goalSport1, goalSport2, goalSport3) 
            VALUES ('$id', '$Monday', '$Tuesday', '$Wednesday', '$Thursday', '$Friday', '$Saturday', '$Sunday', 
            '$lift', '$squat', '$pushup')";
    $result = execute_sql($link, $sql, "graduation_project");
    // if( $result == false ) {
    //     echo "0";
    // }
    // else{
    //     echo "1";
    //     echo "新增成功";
    // }
}
echo "<script type='text/javascript'>";
echo "alert('更新成功');";
echo "location.href='../html/setgoal.php'";		
echo "</script>";
//關閉資料連接	
sqlsrv_close($link);
=======
<?php
session_start();
require_once("dbtools.inc.php");
header("Content-type: text/html; charset=utf-8");

$id = $_SESSION['id'];
$lift = $_POST["lift"]; 
$squat = $_POST["squat"]; 
$pushup = $_POST["pushup"];

if(isset($_POST['weeklyexercise1'])){
    $Monday = "true";
}else{
    $Monday = "false";
}
if(isset($_POST['weeklyexercise2'])){
    $Tuesday = "true";
}else{
    $Tuesday = "false";
}
if(isset($_POST['weeklyexercis3'])){
    $Wednesday = "true";
}else{
    $Wednesday = "false";
}
if(isset($_POST['weeklyexercise4'])){
    $Thursday = "true";
}else{
    $Thursday = "false";
}
if(isset($_POST['weeklyexercise5'])){
    $Friday = "true";
}else{
    $Friday = "false";
}
if(isset($_POST['weeklyexercise6'])){
    $Saturday = "true";
}else{
    $Saturday = "false";
}
if(isset($_POST['weeklyexercise7'])){
    $Sunday = "true";
}else{
    $Sunday = "false";
}
$link = create_connection();

//執行 UPDATE 陳述式來更新使用者資料
$sql = "SELECT * FROM user_goal Where goalID = '$id'";
$result = execute_sql($link, $sql, "graduation_project");
$row = sqlsrv_fetch_array($result, SQLSRV_FETCH_NUMERIC); 
if (sqlsrv_has_rows($result) != 0){

    //釋放 $result 佔用的記憶體
    sqlsrv_free_stmt($result);

    //執行 UPDATE 陳述式來更新使用者資料
    $sql = "UPDATE user_goal SET Monday = '$Monday', Tuesday = '$Tuesday', Wednesday = '$Wednesday', Thursday = '$Thursday', 
    Friday = '$Friday', Saturday = '$Saturday', Sunday = '$Sunday', 
    goalSport1 = '$lift', goalSport2 = '$squat', goalSport3 = '$pushup' WHERE  goalID = '$id'";
    $result = execute_sql($link, $sql, "graduation_project");
    // if( $result == false ) {
    //     echo "0";
    // }
    // else{
    //     echo "1";
    //     echo "更新成功";
    // }
}
else{
    //釋放 $result 佔用的記憶體
    sqlsrv_free_stmt($result);

    //執行 SQL 命令，新增此健身次數
    $sql = "INSERT INTO user_goal (goalID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, 
    goalSport1, goalSport2, goalSport3) 
            VALUES ('$id', '$Monday', '$Tuesday', '$Wednesday', '$Thursday', '$Friday', '$Saturday', '$Sunday', 
            '$lift', '$squat', '$pushup')";
    $result = execute_sql($link, $sql, "graduation_project");
    // if( $result == false ) {
    //     echo "0";
    // }
    // else{
    //     echo "1";
    //     echo "新增成功";
    // }
}
echo "<script type='text/javascript'>";
echo "alert('更新成功');";
echo "location.href='../html/setgoal.php'";		
echo "</script>";
//關閉資料連接	
sqlsrv_close($link);
>>>>>>> origin/main
?>