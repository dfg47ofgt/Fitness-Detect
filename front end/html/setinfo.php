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
//如果 session 中的 passed 變數等於 TRUE
//表示已經登入網站，取得使用者資料	
else
{
require_once("../php/dbtools.inc.php");
$id = $_SESSION['id'];

//建立資料連接
$link = create_connection();

//執行 SELECT 陳述式取得使用者資料
$sql = "SELECT * FROM users Where id = $id";
$result = execute_sql($link, $sql, "graduation_project");
$row = sqlsrv_fetch_array($result, SQLSRV_FETCH_NUMERIC);  
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<title>setinfo</title>
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/Setting.css"/>
<script type="text/javascript">
	function check_data()
	{	
		if (document.myForm.first_name.value.length == 0)
		{
			alert("您一定要留下真實姓名哦！");
			return false;
		}	
		if (document.myForm.last_name.value.length == 0)
		{
			alert("您一定要留下真實姓名哦！");
			return false;
		}	
		if (document.myForm.date.value.length == 0)
		{
			alert("您忘了填「出生」欄位了...");
			return false;
		}
		if(document.getElementById("sex").value == "none")
		{
			alert("您忘了填「性別」欄位了...");
			return false;
		}
		if (document.myForm.cellphone.value.length != 10)
		{
			alert("您的「手機號碼」欄位有誤...");
			return false;
		}
	myForm.submit();
}
</script>
</head>
<body>
<form action="../php/updateinfo.php" method="post" name="myForm">
<div id="setinfo">
	<div id="background"></div>	
	<a href="SET.php">
		<div id="chevron-compact-left_dh" >
			<svg class="backbutton" viewBox="12.378 3.375 10 20">
				<path id="backbutton" d="M 21.68481826782227 3.456463098526001 C 22.30096626281738 3.646719694137573 22.55051040649414 4.108023643493652 22.24260520935059 4.487576961517334 L 15.0247278213501 13.37511444091797 L 22.24482536315918 22.26128578186035 C 22.5544376373291 22.64100074768066 22.30489921569824 23.10321235656738 21.68772506713867 23.29358291625977 C 21.07055282592773 23.48395156860352 20.3194522857666 23.33039283752441 20.01009750366211 22.95059776306152 L 12.51024913787842 13.71973133087158 C 12.3336353302002 13.50284194946289 12.3336353302002 13.247389793396 12.51024913787842 13.0305004119873 L 20.01035308837891 3.799713373184204 C 20.31952095031738 3.420549154281616 21.06914710998535 3.266984701156616 21.68592643737793 3.456464529037476 Z">
				</path>
			</svg>
		</div>
	</a>
	<div id=box>
	<div id="maintitle">
		<span>基本資料</span>
	</div>
<!-- 分隔線 -->
	<svg class="crossline" viewBox="0 0 336 2">
		<path id="crossline" class="crossline" d="M 0 0 L 336 2">
		</path>
	</svg>
	<form action="">
<!-- 姓氏 -->
	<div id="_bk" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="101" height="39">
			</rect>
		</svg>
		<div>
		<input class="inputtitle" type="text" style="width: 91px;" 
			value="<?php echo $row[3] ?>" name="first_name" placeholder="姓氏"/>
		</div>
	</div>

<!-- 名字 -->
	<div id="_bn" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="181" height="39">
			</rect>
		</svg>
		<div>
		<input class="inputtitle" type="text" style="width: 171px;" 
			value="<?php echo $row[4] ?>" name="last_name" placeholder="名字"/>
		</div>
	</div>


<!-- 生理性別 -->
	<div id="_bq" >
		<div>
		<input class="inputtitle" type="text" style="left: 42%; position: absolute;
				overflow: visible;
				height:39px;
				top: 0px; 
				width: 150px;
				background-color:transparent;
				-webkit-text-fill-color: #ffffff;
				opacity: 0.804;
				white-space: nowrap;
				text-align: 10px;
				font-family: Noto Sans CJK TC;
				font-size: 15px;
				font-weight: normal;
				color: rgb(255, 255, 255);
				line-height: 39px;
				z-index: 1;"
			value="<?php echo $row[6] ?>" name="sex" readonly unselectable="on" />
			<!-- <input type="radio" name="gender" value="0">
			<label for="boy">男性</label>&nbsp;&nbsp;&nbsp;&nbsp;
			<input type="radio" name="gender" value="1">
			<label for="girl">女性</label> -->
		</div>
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		
		<div class="inputtitle">
			<span>生理性別</span>
		</div>
	</div>


	<!-- 身高欄位 -->
	<div id="_bt" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div >
			<span class="inputtitle" >身高</span>
			<input type="number" name="height" class="input1" min="0" value="<?php echo $row[7] ?>" style="text-align: center;">
		</div>
		<div id="unitcomment">
			<span>公分</span>
		</div>
	</div>


<!-- 體重欄位 -->
	<div id="_by" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div >
			<span class="inputtitle" >體重</span>
			<input type="number" name="weight" class="input1" min="0" value="<?php echo $row[8] ?>" style="text-align: center;">
		</div>
		<div id="unitcomment">
			<span>公斤</span>
		</div>
	</div>


<!-- 出生日期 -->
	<div id="_ca" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div id="textstyle">
			<div class="inputtitle">
				<span>出生日期</span> 
			</div>
			<div id="textstyle" style="width: 130px; left: 28px; ">
				<div>
				<input type= "date" id="date" name="date" 				
				value="<?php echo $row[5]->format('Y-m-d') ?><?= isset($_POST['date']) ? $_POST['date'] : ''; ?>" name="date" max="<?= date('Y-m-d'); ?>"
				style="position: absolute;
					overflow: auto;
					width: 155px;
					height: 39px;
					z-index: 1;
					left:100px;
					top: 0px; 
					text-align: center;
					background-color:transparent;
					-webkit-text-fill-color: #ffffff;
					color:rgb(0, 0, 0)">
				</div>
			</div>
		</div>
			
	</div>


<!-- 手機號碼 -->
	<div id="_cc" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div class="inputtitle">
			<span>手機號碼</span>
		</div>
		<div>
			<input name="cellphone" class="input1" type="tel" required maxlength="10" 
			value="<?php echo $row[9] ?>"
			style="text-align: center;width: 210px; font-size: 12px; left:28%"  >
		</div>
	</div>


<!-- 電子郵件 -->
	<div id="_ce" >
		<svg class="textframe">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div class="inputtitle">
			<span>電子郵件</span>
		</div>
		<div>
			<input name="email" class="input1" type="email" placeholder="" 
			value="<?php echo $row[10] ?>"
			style="text-align: center; width: 210px; font-size: 12px; left:28%"  >
		</div>
	</div>
</form>


<!-- 確認按鈕 -->
	<div onclick="check_data()" id="_51" >
		<svg class="yellowbutton">
			<rect id="yellowbutton" rx="0" ry="0" x="0" y="0" width="294" height="43">
			</rect>
		</svg>
		<div id="okbutton">
			<span onmouseup="">確認</span>
		</div>
	</div>
</div>
</div>
</form>
</body>
</html>
<?php
    //釋放資源及關閉資料連接
    sqlsrv_free_stmt($result);
    sqlsrv_close($link);
}
?>