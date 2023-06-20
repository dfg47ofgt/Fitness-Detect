<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/qrcode.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/CSS of HM,HR,HSA,PST,PST_running.css"/>
<title>pst_cd</title>
</head>
<body>
<div id="pst_cd">
	<div id="background"></div>
	<!-- 背景 -->
	<div id="box">
		<script>
			　　var t=5;//設定跳轉的時間
			　　setInterval("refer()",1000); //啟動1秒定時
			　　function refer(){
			　　　　if(t==0){
			　　　　　　location="PST_running.php"; //#設定跳轉的鏈接地址
			　　　　}
			　　　　document.getElementById('t').innerHTML=""+t; // 顯示倒計時
			　　　　t--; // 計數器遞減
			　　}

			// 　var tt=0;//設定跳轉的時間
			// 　　setInterval("refer()",1000); //啟動1秒定時
			// 　　function refer(){
			// 　　　　if(tt==5){
			// 　　　　　　location="PST_running.html"; //#設定跳轉的鏈接地址
			// 　　　　}
			// 　　　　document.getElementById('tt').value=tt; // 顯示倒計時
			// 　　　　tt++; // 計數器遞減
			// 　　}
		</script>
		<div style="position: relative; height: 100%; width: 100%">
			<div id="pst_cd_position">
				<div class="ID5" id="t">5</div>
				<!-- <meter id="tt" value="0" min="0" max="4"></meter> -->
				<div class="spinner"></div>
			</div>			
		</div>
	</div>
</div>
</body>
</html>