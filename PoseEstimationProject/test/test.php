<?php 
require_once("dbtools.inc.php");

$var = 6;
$var1 = 12;
$l = exec("python test.py  $var $var1",$Array,$ret);
$k = shell_exec("python test.py  $var $var1");
// print_r ($Array[0]);
// print_r ($Array[1]);
// print_r ($Array[2]);
$userSport1 = $Array[0];
$userSport2 = $Array[1];
$userSport3 = $Array[2];
// echo $userSport1;
// echo $userSport2;
// echo $userSport3;
$userID="123";
$userDate="2020-05-10";
// echo $userID;
// echo $userDate;

//建立資料連接
$link = create_connection();
//釋放 $result 佔用的記憶體
sqlsrv_free_stmt($result);
//執行 SQL 命令，新增使用者健身次數
$sql = "INSERT INTO Fitness_his (userID, userDate, userSport1, userSport2, userSport3) 
        VALUES ('$userID', '$userDate', '$userSport1', '$userSport2', '$userSport3')";
$result = execute_sql($link, $sql, "graduation_project");
// if( $result == false ) {
//   echo "0";
// }
// else{
//   echo "1";
// }
sqlsrv_close($link);
?>