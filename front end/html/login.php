<?php 
session_start();
//檢查 session 中的 passed 變數是否等於 TRUE 
//如果 session 中的 passed 變數等於 TRUE
//表示已登入網站，將使用者導向首頁 HM.html
if (isset($_SESSION['id'])==true)
{
	//顯示訊息提醒使用者即將返回起始畫面
	echo "<script type='text/javascript'>";
	echo "location.href='HM.php'";
	// header("location:main/HM.php");		
	echo "</script>";
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>LG</title>
	<link rel="stylesheet" type="text/css" href="../css/index,login,join.css">
	<script type="text/javascript">
	function check_data()
	{
	if (document.myForm.account.value.length == 0)
		alert("帳號欄位不可以空白哦！");
	else if (document.myForm.password.value.length == 0)
		alert("密碼欄位不可以空白哦！");
	else 
		myForm.submit();
	}	
</script>
</head>
<body>
<div id="LG">
<form action="../php/checkpwd.php" method="post" name="myForm">
	<div id="RGTbackground"></div>
	<a href="../index.html">
		<div style="width: 10px; width: 10px;">
			<img id="_1" src="../picture/_1.png" srcset="../picture/_1.png 1x, ../picture/_1@2x.png 2x">
		</div>
	</a>

	<div id="lgbox">
		<div >
			<div id="__cb">
				<span>歡迎登入</span>
			</div>
			<div>		
				<form >
					<div id="_cd" class="____">
						<svg class="_12_cd">
							<rect id="_12_cd" rx="3" ry="3" x="0" y="0" width="294" height="39">
							</rect>
						</svg>
				
						<div>
							<input name="account" type="text" autocomplete=”off” placeholder="帳號"/>
						</div>
					</div>

					<div id="_6">
						<svg class="_12_cg">
							<rect id="_12_cg" rx="3" ry="3" x="0" y="0" width="294" height="38">
								</rect>
						</svg>
					<div>
						<input name="password" type="text"  autocomplete=”off” placeholder="密碼"/>
					</div>
				</form>
			</div>

		</div>

		<div id="_cn">
			<span>忘記密碼？</span>
		</div>

		<div id="_Fitness_Det">
			<span>如登入，代表同意健身偵探 Fitness Det.使用您提供的所有個人資訊，如：出生年月日、身體基本資訊等</span>
		</div>
		
		<div id="_cj" onmouseup="check_data()">
			<svg class="_12_ck">
				<rect id="_12_ck" rx="3" ry="3" x="0" y="0" width="294" height="38">
				</rect>
			</svg>
			<div id="_cl">
				<span>登入</span>
			</div>
		</div>
	
		<a href="join.php">
			<div id="_cm">
				<span>尚未註冊？加入我們</span>
			</div>
		</a>
	</div>
</form>
</div>
</body>
</html>