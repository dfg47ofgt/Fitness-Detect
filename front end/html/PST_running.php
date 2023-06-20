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

//執行 SELECT 陳述式取得使用者資料
$sql = "SELECT * FROM Fitness_his Where userID = '$id' AND userDate = '$date'";
$result = execute_sql($link, $sql, "graduation_project");
$row = sqlsrv_fetch_array($result, SQLSRV_FETCH_NUMERIC);
if (sqlsrv_has_rows($result) != 0){
	$his_lift = $row[2];
	$his_squat = $row[3];
	$his_pushup = $row[4];
}else{
	$his_lift = "0";
	$his_squat = "0";
	$his_pushup = "0";
}
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/CSS of HM,HR,HSA,PST,PST_running.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<script src="../js/stopwatch.js"></script>
<link rel="stylesheet" href="../cute-alert-master/style.css" />
<script src="../cute-alert-master/cute-alert.js"></script>
<title>pst_running</title>
</head>
<body>
<div id="pst_running">
	<div id="background"></div>
	<div id="box">
		<!-- HM上半部 -->
		<div> 
			<!-- 頭像按鈕 -->
			<a>
				<div id="people-circle_c">
					<svg class="_19_c" viewBox="5.697 22.5 31.282 10.241">
						<path id="dwaw" d="M 36.97872161865234 27.35372352600098 C 34.94717407226562 25.01152229309082 30.47726821899414 22.5 21.33785820007324 22.5 C 12.19845199584961 22.5 7.731086730957031 25.00879096984863 5.696999549865723 27.35463523864746 C 9.493066787719727 30.7618522644043 15.25075721740723 32.74462890625 21.33785820007324 32.74088287353516 C 27.42496681213379 32.74462890625 33.18264770507812 30.7618522644043 36.97872161865234 27.35463523864746 Z">
						</path>
					</svg>
					<svg class="_20_c" viewBox="11.25 6.75 12.289 12.289">
						<path id="dwaw" d="M 17.39452743530273 19.03905868530273 C 20.78805923461914 19.03905868530273 23.53905868530273 16.28805923461914 23.53905868530273 12.89453029632568 C 23.53905868530273 9.500998497009277 20.78805923461914 6.75 17.39452743530273 6.75 C 14.00099945068359 6.75 11.25 9.500998497009277 11.25 12.89453029632568 C 11.25 16.28805923461914 14.00099945068359 19.03905868530273 17.39452743530273 19.03905868530273 Z">
						</path>
					</svg>
					<svg class="_21_da" viewBox="0 0 41.654 41.346">
						<path id="dwaw" d="M 20.82684135437012 2.584153175354004 C 10.76228713989258 2.584153175354004 2.603354215621948 10.6829080581665 2.603354215621948 20.67322731018066 C 2.603354215621948 30.66354751586914 10.76228713989258 38.76229858398438 20.82684135437012 38.76229858398438 C 30.89139747619629 38.76229858398438 39.05033111572266 30.66354751586914 39.05033111572266 20.67322731018066 C 39.05033111572266 10.68290710449219 30.89139366149902 2.584153175354004 20.82684135437012 2.584153175354004 Z M -1.181714878839557e-06 20.67322731018066 C -1.181714878839557e-06 9.255718231201172 9.324496269226074 -2.541146841394948e-06 20.82684326171875 -3.50532957327232e-07 C 32.32918930053711 -3.50532957327232e-07 41.65368270874023 9.255722045898438 41.65368270874023 20.6732292175293 C 41.65368270874023 32.09073638916016 32.32918930053711 41.34645843505859 20.82683563232422 41.34645462036133 C 9.324493408203125 41.34645462036133 -3.388606273801997e-06 32.09073257446289 -1.181714878839557e-06 20.67322540283203 Z">
						</path>
					</svg>
				</div>
			</a>
			<!-- 夥伴名字 -->
			<div id="nameofuser">
				<!--<span>夥伴</span><span id=""> 小黑</span>-->
			</div>
			<div id="_dc">
				<span>開始運動</span>
			</div>
		</div>
		
		<!-- end button -->
			<button onclick="startStop()" id="confirm"> 
				<div>
					<div id="endbuttonposition" >
						<svg class="pstStartButton">
							<ellipse id="pstStartButton" rx="49" ry="49" cx="49" cy="49">
							</ellipse>
						</svg>
						<svg class="_43">
							<rect id="_43" rx="0" ry="0" x="0" y="0" width="52" height="53">
							</rect>
						</svg>
					</div>
				</div>
			</button>

			<script>
				var confirm = document.getElementById("confirm");
					confirm.addEventListener("click", ()=>{
					cuteAlert({
						type: "question",
						title: "結束運動",
						message: "你確定要結束運動嗎？",
						confirmText: "確定",
						cancelText: "繼續運動"
					}).then((e)=>{
						if ( e == ("confirm")){
						location="../php/TrueToFalse.php";
					} else {
						startStop();
				
					}
					})
				})
			</script>

		<!-- start&pause button -->
			<button onclick="startStop()" >
				<div id="startbuttonposition" >
					<!-- 外園 -->
					<svg class="pstStartButton">
						<ellipse id="pstStartButton" rx="49" ry="49" cx="49" cy="49">
						</ellipse>
					</svg>
					<!-- 開始icon -->
					<div id="caret-right-fill">
						<svg class="_39" viewBox="11.25 4.957 45.893 60.13">
							<path id="_39" d="M 55.05001449584961 38.9232063293457 L 21.41956329345703 63.79462432861328 C 17.45534324645996 66.72865295410156 11.25000381469727 64.34316253662109 11.25000381469727 59.89022445678711 L 11.25000381469727 10.14739227294922 C 11.24796867370605 8.111029624938965 12.65593338012695 6.262128353118896 14.84949398040771 5.420634746551514 C 17.04306030273438 4.579140186309814 19.61617660522461 4.900818824768066 21.4277458190918 6.243009090423584 L 55.04455184936523 31.11443519592285 C 56.37808227539062 32.09921264648438 57.1431884765625 33.52309036254883 57.1431884765625 35.01996994018555 C 57.1431884765625 36.516845703125 56.37808227539062 37.94071197509766 55.04455184936523 38.92550659179688 Z">
							</path>
						</svg>
					</div>
					<!-- 暫停icon -->
					<div id="pause-fill">
						<svg class="_38_e" viewBox="9 7.875 44.451 48.052">
							<path id="_38_e" d="M 17.33456802368164 7.875 C 21.93762016296387 7.875 25.66912651062012 11.46062088012695 25.66913223266602 15.88370609283447 L 25.66913223266602 47.91854095458984 C 25.66913223266602 52.34162521362305 21.93762016296387 55.92724609375 17.33456611633301 55.92724609375 C 12.73151111602783 55.92724609375 8.999999046325684 52.34162521362305 8.999999046325684 47.91854095458984 L 9.000001907348633 15.88370800018311 C 9.000001907348633 11.46062088012695 12.73151588439941 7.875 17.33457183837891 7.875 Z M 45.11645889282227 7.875 C 49.71950531005859 7.875 53.45102310180664 11.46062088012695 53.45102310180664 15.88370800018311 L 53.45102310180664 47.91854095458984 C 53.45102310180664 52.34162521362305 49.71950531005859 55.92724609375 45.11645889282227 55.92724609375 C 40.51340484619141 55.92724609375 36.78189086914062 52.34162521362305 36.78189086914062 47.91854095458984 L 36.78189086914062 15.88370800018311 C 36.78189086914062 11.46062088012695 40.51340484619141 7.875 45.11645889282227 7.875 Z">
							</path>
						</svg>
					</div>
				</div>
			</button>

		<!-- 顯示即時運動次數 -->
		<div id="liveshowsport" > 
			<div>
				<span>已經做了 </span><span id="showsport1"><?php echo $his_lift ?></span><span> 下舉啞鈴</span>
			</div>
			<div>
				<span>已經做了 </span><span id="showsport1"><?php echo $his_squat ?></span><span> 下深蹲</span>
			</div>
			<div>
				<span>已經做了 </span><span id="showsport1"><?php echo $his_pushup ?></span><span> 下伏地挺身</span>
			</div>
		</div>
		<!-- 計時器 -->
		<div style="text-align:center;">
			<div  class="stopwatch">
				<span id="hour">00</span>:<span id="min">00</span>:<span id="sec">00</span><span id="milisec" style="font-size: 25px; position: relative; left:5px;">00</span><br>
				<button onclick="reset()">Reset</button>
			</div>  
		</div>
	</div>
</div>
</body>
</html>
<?php
    //釋放資源及關閉資料連接
    sqlsrv_free_stmt($result);
    sqlsrv_close($link);
}
?>