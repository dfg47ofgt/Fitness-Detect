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
	<title>tool</title>
</head>

<body>
	<div id="tool">
		<div id="background"></div>
		<a href="HM.php">
		<div onclick="application.goToTargetView(event)" id="chevron-compact-left">
			<svg class="_24" viewBox="12.378 3.375 10 20">
				<path id="_24"
					d="M 21.68481826782227 3.456463098526001 C 22.30096626281738 3.646719694137573 22.55051040649414 4.108023643493652 22.24260520935059 4.487576961517334 L 15.0247278213501 13.37511444091797 L 22.24482536315918 22.26128578186035 C 22.5544376373291 22.64100074768066 22.30489921569824 23.10321235656738 21.68772506713867 23.29358291625977 C 21.07055282592773 23.48395156860352 20.3194522857666 23.33039283752441 20.01009750366211 22.95059776306152 L 12.51024913787842 13.71973133087158 C 12.3336353302002 13.50284194946289 12.3336353302002 13.247389793396 12.51024913787842 13.0305004119873 L 20.01035308837891 3.799713373184204 C 20.31952095031738 3.420549154281616 21.06914710998535 3.266984701156616 21.68592643737793 3.456464529037476 Z">
				</path>
			</svg>
		</div>
		</a>
		<div id="box">
			<div id="title">
				<span>小工具</span>
			</div>
			<svg class="_5_bl" viewBox="0 0 336 2">
				<path id="_5_bl" d="M 0 0 L 336 2">
				</path>
			</svg>
			<a href="BMI.php">
				<div onclick="application.goToTargetView(event)" id="_" class="___">
					<div id="_8__2" class="___8___2">
						<svg class="barbutton">
							<rect id="barbutton" rx="0" ry="0" x="0" y="0" width="375" height="59">
							</rect>
						</svg>
						<div id="stitle">
							<span>計算BMI</span>
						</div>
						<div id="comment">
							<span>將以你的基本資料計算</span>
						</div>
					</div>
					<img id="arrow" src="../picture/arrow.png" srcset="../picture/arrow.png 1x">
				</div>
			</a>
			<a href="BMR.php">
				<div onclick="application.goToTargetView(event)" id="_33_">
					<div id="_bb" class="___">
						<div id="_8__2_bb" class="___8___2">
							<svg class="barbutton">
								<rect id="barbutton" rx="0" ry="0" x="0" y="0" width="375" height="59">
								</rect>
							</svg>
							<div id="stitle">
								<span>計算基本代謝率</span>
							</div>
							<div id="comment">
								<span>將以你的基本資料計算</span>
							</div>
						</div>
						<img id="arrow" src="../picture/arrow.png" srcset="../picture/arrow.png 1x">
						</svg>
					</div>
				</div>
			</a>
		</div>
	</div>
</body>

</html>