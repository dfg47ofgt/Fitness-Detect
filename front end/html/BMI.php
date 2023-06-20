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
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/bmi,dmr,tool.css" />
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
	<title>BMI</title>
	<script type="text/javascript" src="../js/bmi.js"></script>
</head>

<body>
	<div id="BMI">
		<div id="background"></div>
		<a href="tool.php">
			<div id="BMIbox">
				<div id="chevron-compact-left_bi">
					<svg class="_24_bj" viewBox="12.378 3.375 10 20">
						<path id="_24_bj"
							d="M 21.68481826782227 3.456463098526001 C 22.30096626281738 3.646719694137573 22.55051040649414 4.108023643493652 22.24260520935059 4.487576961517334 L 15.0247278213501 13.37511444091797 L 22.24482536315918 22.26128578186035 C 22.5544376373291 22.64100074768066 22.30489921569824 23.10321235656738 21.68772506713867 23.29358291625977 C 21.07055282592773 23.48395156860352 20.3194522857666 23.33039283752441 20.01009750366211 22.95059776306152 L 12.51024913787842 13.71973133087158 C 12.3336353302002 13.50284194946289 12.3336353302002 13.247389793396 12.51024913787842 13.0305004119873 L 20.01035308837891 3.799713373184204 C 20.31952095031738 3.420549154281616 21.06914710998535 3.266984701156616 21.68592643737793 3.456464529037476 Z">
						</path>
					</svg>
				</div>
		</a>
		<div id="box">
			<div id="title">
				<span>計算BMI</span>
			</div>
			<svg class="_5_bl" viewBox="0 0 336 2">
				<path id="_5_bl" d="M 0 0 L 336 2">
				</path>
			</svg>
			<form action="">
				<div id="_bm" class="____">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>
					<div>
						<span class="inputtitle">身高</span>
						<input id="height" type="number" min="0" value="0" class="input">
					</div>
					<div class="unitcomment">
						<span>公分</span>
					</div>
				</div>
				<div id="_bp" class="____">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>
					<div>
						<span class="inputtitle">體重</span>
						<input id="weight" type="number" min="0" value="0" class="input">
					</div>
					<div class="unitcomment">
						<span>公斤</span>
					</div>
				</div>
				<div id="_27_cb" onclick="countBMI()">
					<svg class="_27_cb">
						<rect id="_27_cb" rx="3" ry="3" x="0" y="0" width="294" height="43">
						</rect>
					</svg>
					<div id="_ce" >
						<span>計算</span>
					</div>
				</div>
			</form>
			<div id="BMIcommend">
				<span>國民健康署建議我國成人 BMI應維持在 18.5 及 24 之間。體重過輕：BMI小於18.5、健康體位：BMI介於18.5與24之間、過重：BMI大於24。</span>
				<br>
			</div>
			<!-- Show BMI -->
			<div id="textstyle" style="left:41px; top: 230px;">
				<svg class="textframe" style="left:45px">
					<rect id="textframe" rx="3" ry="3" x="0" y="0" width="237" height="39" >
					</rect>
				</svg>
				<div>
					<span id="text" style="left:116px" class="input">---</span>
					<span id="index" style="left: 20px;" class="input">---</span>
				</div>
				<div class="unitcomment" style="left: 240px;">
					<span>kg/m2</span>
				</div>
			</div>
			<div id="BMI_bx" >
				<span>BMI：</span>
			</div>
		</div>
	</div>
</div>
</body>

</html>