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
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" id="applicationStylesheet"  href="../css/Setting.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<title>SET</title>
</head>
<body>
<div id="SET">
	<div id="background"></div>	
		<a href="HM.php">
			<div id="chevron-compact-left_dh" >
				<svg class="backbutton" viewBox="12.378 3.375 10 20">
					<path id="backbutton" d="M 21.68481826782227 3.456463098526001 C 22.30096626281738 3.646719694137573 22.55051040649414 4.108023643493652 22.24260520935059 4.487576961517334 L 15.0247278213501 13.37511444091797 L 22.24482536315918 22.26128578186035 C 22.5544376373291 22.64100074768066 22.30489921569824 23.10321235656738 21.68772506713867 23.29358291625977 C 21.07055282592773 23.48395156860352 20.3194522857666 23.33039283752441 20.01009750366211 22.95059776306152 L 12.51024913787842 13.71973133087158 C 12.3336353302002 13.50284194946289 12.3336353302002 13.247389793396 12.51024913787842 13.0305004119873 L 20.01035308837891 3.799713373184204 C 20.31952095031738 3.420549154281616 21.06914710998535 3.266984701156616 21.68592643737793 3.456464529037476 Z">
					</path>
				</svg>
			</div>
			</a>
				<div id=setbox>
			<div id="maintitle">
				<span>設定</span>
			</div>
			<svg class="crossline" viewBox="0 0 336 2">
				<path id="crossline" d="M 0 0 L 336 2">
				</path>
			</svg>

	<!-- 運動目標 -->
	<a href="setgoal.php">
		<div id="_43">
			<div onclick="" id="_8__7" class="___8___7">
				<svg class="_33_d">
					<rect id="_33_d" rx="0" ry="0" x="0" y="0" width="340" height="59">
					</rect>
				</svg>
				<div id="stitle">
					<span>運動目標</span>
				</div>
			</div>
			<img id="arrow" src="../picture/arrow.png" srcset="../picture/arrow.png 1x">
				
			</svg>
			<div id="comment">
				<span>設定每日動作次數與運動時間。</span>
			</div>
		</div>
		</a>

	<!-- 基本資料 -->
	<a href="setinfo.php">
		<div id="_34">
			<svg class="_33_dt">
				<rect onclick="application.goToTargetView(event)" id="_33_dt" rx="0" ry="0" x="0" y="0" width="340" height="59">
				</rect>
			</svg>
			<div id="stitle">
				<span>基本資料</span>
			</div>
			<div id="comment">
				<span>更改、設定基本資料。</span>
			</div>
			<img id="arrow" src="../picture/arrow.png" srcset="../picture/arrow.png 1x">
				
			</svg>
		</div>
	</a>


	<!-- 變更密碼 -->
	<a href="setpassword.php">
		<div id="_36">
			<div onclick="" id="_8__7" class="___8___7">
				<svg class="_33_d">
					<rect id="_33_d" rx="0" ry="0" x="0" y="0" width="340" height="59">
					</rect>
				</svg>
				<div id="stitle">
					<span>變更密碼</span>
				</div>
			</div>
			<img id="arrow" src="../picture/arrow.png" srcset="../picture/arrow.png 1x">
				
			</svg>
			<div id="comment">
				<span>重新設定密碼。</span>
			</div>
		</div>
		</a>



	<!-- 健身日期 -->
	<div id="_45_ea" >
		<svg class="_31">
			<rect id="_31" rx="0" ry="0" x="0" y="0" width="340" height="59">
			</rect>
		</svg>
		<label id ="timesup" class="switch">
			<input type="checkbox" 	>
			<span class="slider round"></span>
		</label>  
		<div id="stitle">
			<span>健身提醒</span>
		</div>
		<div id="comment">
			<span>當運動時間到，傳送提醒給我。</span>
		</div>
	</div>


	<!-- 計數提醒 -->
	<div id="_45" >
		<svg class="_33_ec">
			<rect id="_33_ec" rx="0" ry="0" x="0" y="0" width="340" height="59">
			</rect>
		</svg>
		<label id ="goalsup" class="switch">
			<input type="checkbox" >
			<span class="slider round"></span>
		</label>  
		<div id="stitle">
			<span>計數提醒</span>
		</div>
		<div id="comment">
			<span>當次數目標達到，傳送提醒給我。</span>
		</div>
	</div>


	<!-- 登出 -->
	<div  id="_dg" >
		<a href="../php/clear.php">
			<svg class="_41">
				<rect id="_41" rx="0" ry="0" x="0" y="0" width="294" height="43">
				</rect>
			</svg>
			<div id="_42" >
				登出
			</div>
		</a>
	</div>
</div>
</div>
</body>
</html>