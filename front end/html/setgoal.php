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

//建立資料連接
$link = create_connection();

//執行 SELECT 陳述式取得使用者資料
$sql = "SELECT * FROM user_goal Where goalID = '$id'";
$result = execute_sql($link, $sql, "graduation_project");
$row = sqlsrv_fetch_array($result, SQLSRV_FETCH_NUMERIC);
if (sqlsrv_has_rows($result) != 0){
	$goal_lift = $row[8];
	$goal_squat = $row[9];
	$goal_pushup = $row[10];
}else{
	$goal_lift = "0";
	$goal_squat = "0";
	$goal_pushup = "0";
}
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/Setting.css"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<title>setgoal</title>
<script type="text/javascript">
	function check_data()
	{	
		myForm.submit();
	}
</script>
</head>
<body>
<form action="../php/checksportsgoal.php" method="post" name="myForm">
<div id="setgoal">
	<div id="background"></div>		
	<!-- 上一頁箭頭 -->	
	<a href="SET.php"> 
		<div id="chevron-compact-left_dh" >
			<svg class="backbutton" viewBox="12.378 3.375 10 20">
				<path id="backbutton" d="M 21.68481826782227 3.456463098526001 C 22.30096626281738 3.646719694137573 22.55051040649414 4.108023643493652 22.24260520935059 4.487576961517334 L 15.0247278213501 13.37511444091797 L 22.24482536315918 22.26128578186035 C 22.5544376373291 22.64100074768066 22.30489921569824 23.10321235656738 21.68772506713867 23.29358291625977 C 21.07055282592773 23.48395156860352 20.3194522857666 23.33039283752441 20.01009750366211 22.95059776306152 L 12.51024913787842 13.71973133087158 C 12.3336353302002 13.50284194946289 12.3336353302002 13.247389793396 12.51024913787842 13.0305004119873 L 20.01035308837891 3.799713373184204 C 20.31952095031738 3.420549154281616 21.06914710998535 3.266984701156616 21.68592643737793 3.456464529037476 Z">
				</path>
			</svg>
		</div>
	</a>
	<div id=box>	
	<!-- title -->
	<div id="maintitle">
		<span>運動目標</span>
	</div>
	<!-- 分隔線 -->
	<svg class="crossline" viewBox="0 0 336 2">
		<path id="crossline" d="M 0 0 L 336 2">
		</path>
	</svg>
<form action="">
	<div id="_46">
		<span class="inputtitle" >每週運動日</span>
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>	
		<div style="position: absolute ;left: 31%; top: 50%; transform: translateY(-50%)">
			<label>
				<input type="checkbox" name="weeklyexercise7" id ="Sunday" value="sun">
				<span style="font-size: 14px;">日</span>
			</label>
			<label>
				<input type="checkbox" name="weeklyexercise1" id="Monday" value="mon" >
				<span style="font-size: 14px;">一</span>
			</label>
			<label>
				<input type="checkbox" name="weeklyexercise2" id ="Tuesday" value="tue" >
				<span style="font-size: 14px;">二</span>
			</label>
			<label>
				<input type="checkbox" name="weeklyexercise3" id ="Wednesday" value="wed" >
				<span style="font-size: 14px;">三</span>
			</label>
			<label>
				<input type="checkbox" name="weeklyexercise4" id ="Thursday" value="thu" >
				<span style="font-size: 14px;">四</span>
			<label>
				<label>
				<input type="checkbox" name="weeklyexercise5" id ="Friday" value="fri" >
				<span style="font-size: 14px;">五</span>
			</label>
			<label>
				<input type="checkbox" name="weeklyexercise6" id ="Saturday" value="sat" >
				<span style="font-size: 14px;">六</span>
			</label>
		</div>
	</div>
	<!-- 每日運動時間 -->
	<div id="_48">
		<div id="_cw" >
			<svg class="textframe">
				<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
				</rect>
			</svg>
			<div id="textstyle" style="width: 130px; left: 0px; ">
				<span class="inputtitle">每日運動時間</span>
				<input type="time" class="input1" 	
				style="position: absolute;
				overflow: auto;
				width: 155px;
				height: 39px;
				z-index: 1;
				left: 120px;
				top: 0px; 
				text-align: center;
				background-color:transparent;
				-webkit-text-fill-color: #ffffff;
				color:rgb(255, 255, 255)">
			</div>
		</div>
	</div>
	<!-- 舉啞鈴次數 -->
	<div id="_47">
		<div id="_cr" >
			<svg class="textframe">
				<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
				</rect>
			</svg>
			<div >
				<span class="inputtitle">舉啞鈴次數</span>
				<input type="number" name="lift" class="input1"  min="0" value="<?php echo $goal_lift ?>" style="text-align: center;">
				</div>
			
			<div id="unitcomment" style="left: 255px">
				<span>次/天</span>
			</div>
		</div>
	</div>
	<!-- 深蹲次數 -->
	<div id="_49">
		<div id="_c" >
			<svg class="textframe">
				<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
				</rect>
			</svg>
			<div >
				<span  class="inputtitle" >深蹲次數</span>
				<input type="number" name="squat" class="input1" min="0" value="<?php echo $goal_squat ?>" style="text-align: center;">
			</div>
			<div id="unitcomment" style="left: 255px">
				<span>次/天</span>
			</div>
		</div>
	</div>
	<!-- 伏地挺身次數 -->
	<div id="_50">
		<div id="_db" >
			<svg class="textframe">
				<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
				</rect>
			</svg>
			<div>
				<span  class="inputtitle" >伏地挺身次數</span>
				<input type="number" name="pushup" class="input1" min="0" value="<?php echo $goal_pushup ?>" style="text-align: center;">
			</div>
			<div id="unitcomment" style="left: 255px">
				<span>次/天</span>
			</div>
		</div>
	</div>
	<!-- 確認按鈕 -->
	<button id="_52" onclick="check_data()">
	<!-- <div id="_52" onclick=""> -->
	<!-- <a href="../php/checksportgoal.php"> -->
		<svg class="yellowbutton">
			<rect id="yellowbutton" rx="0" ry="0" x="0" y="0" width="294" height="43">
			</rect>
		</svg>
		<div id="okbutton">
			<span>確認</span>
		</div>
		<!-- </a> -->
	</button>
</div>	
</form>
</div>
<!-- </form> -->
</body>
</html>
<?php
    //釋放資源及關閉資料連接
    sqlsrv_free_stmt($result);
    sqlsrv_close($link);
}
?>