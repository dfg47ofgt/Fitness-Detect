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
header("Content-type: text/html; charset=utf-8");

//建立資料連接
$link = create_connection();
$id = $_SESSION['id'];

//執行 SELECT 陳述式取得使用者資料
$sql = "SELECT * FROM users Where id = $id";
$result = execute_sql($link, $sql, "graduation_project");
$row = sqlsrv_fetch_array( $result, SQLSRV_FETCH_NUMERIC);
$game = "-GAME";
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ko" lang="ko">
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/qrcode.js"></script>
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/CSS of HM,HR,HSA,PST,PST_running.css"/>
<title>pst</title>
<!--<script type="text/javascript">
    function onload_data() {
        alert("請將 QRcord 條碼對準攝像頭2至3秒");
    }
</script>-->
</head>
<body onload="onload_data()">
<div id="pst">
	<div id="background"></div>
	<div id="box" style="background-color: rgba(112, 112, 112, 0.8);">
		<!-- 框框線 -->
		<svg class="_27">
			<rect id="_27" rx="43" ry="43" x="0" y="0" width="295" height="295">
			</rect>
		</svg>
		<div style="z-index:3; position:absolute; top: 190px ;left: 75px;" >
			<input id="text" type="text" value="<?php echo "$row[1]$game"?>"+ style="width:max-content" disabled="disabled"/>
			<div id="qrcode"></div>
		</div>
		<script type="text/javascript">
			var qrcode = new QRCode(document.getElementById("qrcode"), {
				width : 225,
				height : 225
			});
			function makeCode () {		
				var elText = document.getElementById("text");		
					if (!elText.value) {
						alert("Input a text");
						elText.focus();
						return;
					}
				qrcode.makeCode(elText.value);
			}
			makeCode();
			// css
			$("#text"). 
				on("blur", function () {
					makeCode();
				}).
				on("keydown", function (e) {
					if (e.keyCode == 13) {
						makeCode();
					}
				});
		</script>
		<!--<div id="定位">
		<span onclick="location='../php/checkqrcord.php'">確認定位</span></a>
		</div> -->
		<!-- 文字提醒 -->
		<!-- <div id="scanSuccess"style="position: absolute; top: 65%; left: 60%; z-index: 2;">
			<button onclick="scanSuccess()">
			按一下，假裝好掃描確定
			</button>
		</div> -->
		<!-- 離開按鈕 -->
		<a href="HM.php">
			<img id="_6_ce" src="../picture/exitbutton.png" srcset="../picture/exitbutton.png 1x, ../picture/exitbutton@2x.png 2x">
		</a>
		<!-- 下圖白塊 -->
		<div id="_29"></div>
		<!-- 文字提醒 -->
		<!--<div id="__cg">
			<span>掃描行動條碼，好讓健身偵探確認你所使用的器材定位！<br/>待掃瞄完畢，自動開始健身！</span>
		</div>-->
	</div>
</div>

<script>
	　function scanSuccess(){
　　　　　　	location="PST_cd.php"; }
</script>
</body>
</html>
<?php
    //釋放資源及關閉資料連接
    sqlsrv_free_stmt($result);
    sqlsrv_close($link);
}
?>