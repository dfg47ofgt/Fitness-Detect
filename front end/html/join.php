<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RGT</title>
<link rel="stylesheet" type="text/css" href="../css/index,login,join.css">
<script type="text/javascript">
		function check_data()
		{	
			if (document.myForm.account.value == 0)
			{
				alert("「使用者帳號」一定要填寫哦...");
				return false;
			}
			if (document.myForm.account.value.length == 0)
			{
				alert("「使用者帳號」一定要填寫哦...");
				return false;
			}
			if (document.myForm.account.value.length > 10)
			{
				alert("「使用者帳號」不可以超過 10 個字元哦...");
				return false;
			}
			if (document.myForm.password.value.length == 0)
			{
				alert("「使用者密碼」一定要填寫哦...");
				return false;
			}
			if (document.myForm.password.value.length > 10)
			{
				alert("「使用者密碼」不可以超過 10 個字元哦...");
				return false;
			}
			if (document.myForm.re_password.value.length == 0)
			{
				alert("「密碼確認」欄位忘了填哦...");
				return false;
			}
			if (document.myForm.password.value != document.myForm.re_password.value)
			{
				alert("「密碼確認」欄位與「使用者密碼」欄位一定要相同...");
				return false;
			}
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
			// var date = document.getElementById("date").value
            // alert(date);
			if(document.getElementById("checkbox").checked == 0)
			{
				alert("您忘了勾選同意此服務了...");
				return false;
			}
        myForm.submit();
    }
	</script>
</head>
<body>
<div id="RGT">
<form action="../php/addmember.php" method="post" name="myForm">
	<!-- 離開按鈕 -->
	<div id="RGTbackground"></div>
		<a href="../index.html">
			<div style="width: 10px; width: 10px;">
				<img id="_1" src="../picture/_1.png" srcset="../picture/_1.png 1x, ../picture/_1@2x.png 2x">
			</div>
		</a>

	<div id="box">
		<div >
			<div id="成為健身夥伴" >
				<span>成為健身夥伴</span>
			</div>
			
			<div id="文字敘述" >
				<span>建立個人檔案，獲取最新功能，<br/>讓Fitness Det. 優化你的健身體驗！</span>
			</div>

			<div>
				<form> 
					<!-- 輸入帳號 -->
					<div id="textstyle" > 
						<svg class="_12" >
							<rect id="_12" rx="3" ry="3" x="0" y="0" width="294" height="39">
							</rect>
						</svg>
						<div>
							<input name="account" type="text" autocomplete=”off”  placeholder="帳號"/>
						</div>
					</div>

					<!-- 輸入密碼 -->
					<div id="textstyle"> 
						<svg class="_12_bi">
							<rect id="_12_bi" rx="3" ry="3" x="0" y="0" width="294" height="39">
							</rect>
						</svg>
						<div>
							<input name="password" type="text" autocomplete=”off”  placeholder="密碼"/>
						</div>
					</div>

					<!-- 再次輸入密碼 -->
					<div id="textstyle">
						<svg class="_12_bl">
							<rect id="_12_bl" rx="3" ry="3" x="0" y="0" width="294" height="39">
							</rect>
						</svg>
						<div>
							<input name="re_password" type="text"  autocomplete=”off” placeholder="再次確認密碼"/>
						</div>
					</div>

					<div style="display: flex;">
						<!-- 姓氏 -->
						<div id="_bq">
							<svg class="textframe1">
								<rect id="textframe" rx="3" ry="3" x="0" y="0" width="105" height="39">
								</rect>
							</svg>
							<div>
								<input name="first_name" type="text" autocomplete=”off” style="width: 105px; top: -43px;" placeholder="姓氏"/>
							</div>
						</div>
						
						<!-- 名字 -->
						<div id="_bt">
							<svg class="textframe1">
								<rect id="textframe" rx="3" ry="3" x="0" y="0" width="181" height="39">
								</rect>
							</svg>
							<div>
								<input name="last_name" type="text" autocomplete=”off” style="width: 181px; top: -43px;" placeholder="名字"/>
							</div>
						</div>
					</div>
		
					<div style="display: flex;">
						<!-- 出生日期 -->
						<div id="textstyle"  style="width: 200px;"> 
							<div>
								<span id="whitetext" style="left:10px; line-height:39px; font-size: 13px;" >生日</span> 
							</div>

							<svg class="textframe1" style="width: 200px; position: absolute;">
								<rect id="textframe" rx="3" ry="3" x="0" y="0" width="200" height="39">
								</rect>
							</svg>
						
							<div style="width: 130px;">
									<div>
									<input type= "date" id="date" name="date" value="<?= isset($_POST['date']) ? $_POST['date'] : ''; ?>" name="date" max="<?= date('Y-m-d'); ?>"
										style="position: absolute;
										overflow: auto;
										width: 130px;
										height: 39px;
										z-index: 1;
										left:60px;
										background-color:transparent;
										-webkit-text-fill-color: #ffffff;
										color:rgb(187, 187, 187)">
									</div>
							</div>
						</div>
					
						<!-- 性別 -->
						<div id="textstyle" style="width: 84px; margin-left: 0px;"> 
							<svg class="textframe1" style="width: 84px; position: absolute;">
								<rect id="textframe" rx="3" ry="3" x="0" y="0" width="84" height="39">
								</rect>
							</svg>
							<div>
							<label for="sex-select"></label>
								<select id="sex" name="sex" style="position: absolute;
								height: 39px;
								width: 74px;
								background-color:transparent;
								-webkit-text-fill-color: #ffffff;
								color:rgb(187, 187, 187);" > 
										<option selected="true" disabled="true" value="none">生理性別</option>
										<option value="男性">男性</option>
										<option value="女性">女性</option>
								</select>
							</div>

						</div>
					</div>
					
					<!-- 勾選以示同意 -->
					<div style="width: 254px; height: 40px; position: relative; margin-left: 10px;">
						<div id="_3__1">
							<input id="checkbox" name="checkbox" type="checkbox" style="z-index: 1; width: 19px; height: 19px ;top: 25% "  >	
						</div>
						<div id="勾選">
							<div id="__bz">
								<span>勾選，代表同意本軟體使用以上資訊建立會員資料庫，同時僅使用於本軟體服務</span><br>
							</div>
						</div>
					</div>
				</form>

				<!-- 加入按鈕 -->
				<div onmouseup="check_data()" id="_b" style="margin: 0 10px 5px 10px ;" >
					<svg class="_12_b">
						<rect id="加入" rx="3" ry="3" x="0" y="0" width="294" height="38">
						</rect>
					</svg>
					<div id="_ca">
						<span>加入</span>
					</div>
				</div>

				<!-- 跳回登入頁 -->
				<a href="login.php">
					<div id="已有帳號">
						<span>已經有帳號？登入</span>
					</div>
				</a>
			</div>
		</div> 
	</div>
	</form>
</div>
</body>
</html>