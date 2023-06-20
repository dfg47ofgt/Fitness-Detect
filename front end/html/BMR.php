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
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
	<title>Bmr</title>
	<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/bmi,dmr,tool.css" />
	<script type="text/javascript" src="../js/bmi.js"></script>
</head>

<body>
	<div id="Bmr">
		<div id="background"></div>
		<a href="tool.php">
			<div onclick="application.goToTargetView(event)" id="chevron-compact-left_b">
				<svg class="_24_b" viewBox="12.378 3.375 10 20">
					<path id="_24_b"
						d="M 21.68481826782227 3.456463098526001 C 22.30096626281738 3.646719694137573 22.55051040649414 4.108023643493652 22.24260520935059 4.487576961517334 L 15.0247278213501 13.37511444091797 L 22.24482536315918 22.26128578186035 C 22.5544376373291 22.64100074768066 22.30489921569824 23.10321235656738 21.68772506713867 23.29358291625977 C 21.07055282592773 23.48395156860352 20.3194522857666 23.33039283752441 20.01009750366211 22.95059776306152 L 12.51024913787842 13.71973133087158 C 12.3336353302002 13.50284194946289 12.3336353302002 13.247389793396 12.51024913787842 13.0305004119873 L 20.01035308837891 3.799713373184204 C 20.31952095031738 3.420549154281616 21.06914710998535 3.266984701156616 21.68592643737793 3.456464529037476 Z">
					</path>
			</svg>
			</div>
		</a>
		<form action="">
			<div id="box">
				<div id="title">
					<span>計算基本代謝率</span>
				</div>
				<svg class="_5_bl" viewBox="0 0 336 2">   
					<path id="_5_bl" d="M 0 0 L 336 2">
					</path>
				</svg>
				
				<div id="_ca">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>
					<div>
						<span class="inputtitle" >身高</span>
						<input type="number" id="height" min="0" value="0" class="input">
					</div>
					<div class="unitcomment">
						<span>公分</span>
					</div>
				</div>

				<div id="_cc">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>
					<div>
						<span class="inputtitle" >體重</span>
						<input type="number" id="weight" min="0" value="0" class="input">
					</div>
					<div class="unitcomment">
						<span>公斤</span>
					</div>
				</div>

				<div id="_28">
					<div id="_cg" >
						<svg class="_12_ch" style="left:128px">
							<rect id="_12_ch" rx="3" ry="3" x="0" y="0" width="166" height="39">
							</rect>
						</svg>
						<span id="tdee_out" style="left:128px" class="input">---</span>
						<div id="_ci">
							<span>每日總熱量消耗：</span>
						</div>

					</div>
					<div class="unitcomment" style="left: 250px;">
						<span>Kcal</span>
					</div>
				</div>
				<div id="_ck">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>

					<div>
						<span class="inputtitle">年齡</span>
						<input type="number" id="age" min="0" value="0" class="input">
					</div>
					<div class="unitcomment">
						<span>歲</span>
					</div>
				</div>
				<div id="_cn">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>
					<div id="textstyle" >
						<div class="inputtitle" >
							<span>日常活動等級</span>
						</div>
						<label for="activity"></label>
						<select id="activity-level" style="position: absolute;
						overflow: auto;
						width: 138px;
						height: 39px;
						left: 125px; 
						top: 0px; 
						text-align-last:left;
						background-color:transparent;
						-webkit-text-fill-color: #ffffff;
						color:rgb(187, 187, 187);">
							<option value="none">選擇活動等級</option>
							<option value="1.2">久坐</option>
							<option value="1.375">輕量活動量</option>
							<option value="1.55">中度活動量</option>
							<option value="1.72">高度活動量</option>
							<option value="1.9">非常高度活動量</option>
						</select>
					</div>
					
				</div>
				<div id="_cq">
					<svg class="textframe">
						<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
						</rect>
					</svg>

					<div id="gender" style="left:42%" class="input">
						<input type="radio" name="gender" value="boy" id="male">
						<label for="boy">男性</label>&nbsp;&nbsp;&nbsp;&nbsp;
						<input type="radio" name="gender" value="girl" id="female">
						<label for="girl">女性</label>
					</div>

					<div class="inputtitle">
						<span>生理性別</span>
					</div>
				</div>

				<span id="_cf">基本代謝率為人體一天至少消耗的熱量，此數值會依年紀、性別、肌肉量而有所差異。此計算為基本數值計算，仍需依專業射量機器計算為準。</span>
			
				<div id="_27_cb" onclick="countTDEE()" >
					<svg class="_27_cb">
						<rect id="_27_cb" rx="3" ry="3" x="0" y="0" width="294" height="43">
						</rect>
					</svg>
					<div id="_ce" >
						<span>計算</span>
					</div>
				</div>
			</div>
		</form>
	</div>
</body>

</html>