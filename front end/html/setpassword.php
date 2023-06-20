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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">

<title>setpassword</title>
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/Setting.css"/>
<script type="text/javascript">
	function check_set_data()
	{
	if (document.myForm.oldpassword.value.length == 0)
		alert("「舊密碼」欄位不可以空白哦！");
	else if (document.myForm.newpassword.value.length == 0)
		alert("「新密碼」欄位不可以空白哦！");
	else if (document.myForm.re_newpassword.value.length == 0)
		alert("「確認新密碼」欄位不可以空白哦！");
	else if (document.myForm.newpassword.value != document.myForm.re_newpassword.value)
		alert("「新密碼」欄位與「確認新密碼」要相同哦！");
	else if (document.myForm.oldpassword.value == document.myForm.newpassword.value)
		alert("「舊密碼」與「新密碼」不能相同哦！");
	else 
		myForm.submit();
	}	
</script>
</head>
<body>
<form action="../php/checksetpwd.php" method="post" name="myForm">
<div id="setpassword">
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
		<span>變更密碼</span>
	</div>
	<svg class="crossline" viewBox="0 0 336 2">
		<path id="crossline" d="M 0 0 L 336 2">
		</path>
	</svg>

	

	<!-- 輸入舊密碼 -->
	<div id="_" >
		<svg class="_12">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div>
			<input  name="oldpassword" class="inputtitle" type="password" placeholder="輸入舊密碼"color:white;>
		</div>
	</div>

	<!-- 輸入新密碼 -->
	<div id="_bb" >
		<svg class="_12_">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div >
			<input name="newpassword" class="inputtitle" type="password" placeholder="輸入新密碼">
		</div>
	</div>

	<!-- 確認新密碼 -->
	<div id="_bd" >
		<svg class="_12_ba">
			<rect id="textframe" rx="3" ry="3" x="0" y="0" width="294" height="39">
			</rect>
		</svg>
		<div >
			<input name="re_newpassword" class="inputtitle" type="password" placeholder="確認新密碼">
		</div>
	</div>

	<!-- 確認按鈕 -->
	<div onclick="" id="_bf" >
		<svg class="yellowbbutton">
			<rect id="yellowbutton" rx="3" ry="3" x="0" y="0" width="294" height="38">
			</rect>
		</svg>
		<div id="okbutton">
			<span onmouseup="check_set_data()">確認</span>
		</div>
	</div>
	
</div>
</div>
</form>
</body>
</html>