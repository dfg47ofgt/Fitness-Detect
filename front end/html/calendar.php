<?php 
session_start();
//檢查 session 中的 passed 變數是否等於 TRUE 
//如果 session 中的 passed 變數不等於 TRUE
//表示尚未登入網站，將使用者導向首頁 index.html
if (isset($_SESSION['id'])==false)
{
	//顯示訊息提醒使用者即將返回起始畫面
	echo "<script type='text/javascript'>";
	echo "alert('尚未登入，即將返回起始畫面');";
	echo "location.href='../index.html'";		
	echo "</script>";
}
else
{
require_once("../php/dbtools.inc.php");

$id = $_SESSION['id'];
$date = date("Y-m-d", time()+8*60*60);
//建立資料連接
$link = create_connection();
$sql = "SELECT * FROM Fitness_his Where userID = '$id'";
$result = execute_sql($link, $sql, "graduation_project");
$count = 0;
$sum = 0;
$arrayDate = array();
$arraySport1 = array();
$arraySport2 = array();
$arraySport3 = array();
while( $row = sqlsrv_fetch_array( $result, SQLSRV_FETCH_ASSOC) ) {
    $testDate[] = $row['userDate']->format('Y-m-d');
    $testSport1[] = $row['userSport1'];
    $testSport2[] = $row['userSport2'];
    $testSport3[] = $row['userSport3'];
    $count+=1;
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arrayDate,"$testDate[$sum]");
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport1,"$testSport1[$sum]");
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport2,"$testSport2[$sum]");
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport3,"$testSport3[$sum]");   
}
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>無標題文件</title>
<div id="calendar"></div>
<script src="../js/moment.js"></script>
<script src="../js/javascript.js"></script>
<script type="text/javascript">
 //js呼叫php變數
 var userCount ="<?php echo $count; ?>" ; //賦值
 var userSport1 =<?php echo json_encode($arraySport1); ?> ; //賦值
 var userSport2 =<?php echo json_encode($arraySport2); ?> ; //賦值
 var userSport3 =<?php echo json_encode($arraySport3); ?> ; //賦值
 var userDate =<?php echo json_encode($arrayDate); ?> ; //賦值

!function() {
    var data = [];
    for(i=0;i<userCount;i++){
        if(userSport1[i] != 0){
            data.push({
                eventName : "Left Lift : "+userSport1[i],
                calendar : 'Left Lift',
                color : 'orange',
                date : userDate[i]
            });
        }
        if(userSport2[i] != 0){
            data.push({
                eventName : "Right Lift : "+userSport2[i],
                calendar : 'Right Lift',
                color : 'blue',
                date : userDate[i]
            });
        }
        if(userSport3[i] != 0){
            data.push({
                eventName : "Squat : "+userSport3[i],
                calendar : 'Squat',
                color : 'green',
                date : userDate[i]
            });
        }
    }

    // var data = [
    //     { eventName: "做了"+userSport1[2]+"下深蹲", calendar: 'Squat', color: 'orange' ,date:userDate[2]},
    //     { eventName: "做了"+userSport2[2]+"下挺舉", calendar: 'Deadlifts', color: 'blue' ,date:userDate[2]},
    //     { eventName: "做了"+userSport3[2]+"下臥舉", calendar: 'clean and jerk', color: 'green',date:userDate[2]}
    // ];
function addDate(ev) {
}

var calendar = new Calendar('#calendar', data);
}();

</script>
<link rel="stylesheet" type="text/css" href="../css/style.css">
</head>
</html>
<?php
    //釋放資源及關閉資料連接
    sqlsrv_free_stmt($result);
    sqlsrv_close($link);
}
?>