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
else
{
require_once("../php/dbtools.inc.php");

$id = $_SESSION['id'];
$date = date("Y-m-d", time()+8*60*60);
//建立資料連接
$link = create_connection();
$sql = "SELECT * FROM Fitness_his Where userID = '$id'";
$result = execute_sql($link, $sql, "graduation_project");
$count = 0;
$sum = 0;
$arrayDate = array();
$arraySport1 = array();
$arraySport2 = array();
$arraySport3 = array();
$arraySport4 = array();
while( $row = sqlsrv_fetch_array( $result, SQLSRV_FETCH_ASSOC) ) {
    $testDate[] = $row['userDate']->format('Y-m-d');
    $testSport1[] = $row['userSport1'];
    $testSport2[] = $row['userSport2'];
    $testSport3[] = $row['userSport3'];
	$testSport4[] = $row['userSport4'];
    $count+=1;
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arrayDate,"$testDate[$sum]");
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport1,"$testSport1[$sum]");
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport2,"$testSport2[$sum]");
    for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport3,"$testSport3[$sum]");  
	for($i=0;$i<=$count-1;$i++)
    $sum = $i;
    array_push($arraySport4,"$testSport4[$sum]");   		
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
<link rel="stylesheet" type="text/css" id="applicationStylesheet" href="../css/CSS of HM,HR,HSA,PST,PST_running.css"/>
<link rel="stylesheet" href="../watchout/style.css" />
<script src="../watchout/cute-alert.js"></script>
<script src="../js/moment.min.js"></script>
<link rel="stylesheet" type="text/css" href="../css/hrstyle.css">


<title>HR</title>

</head>
<body>
<div id="HR">
	<div id="background"></div>

	<div id="box">
		
		<div id="maintitle">
			<span>運動紀錄</span>
		</div>
		<svg class="crossline" viewBox="0 0 336 2">
			<path id="crossline" d="M 0 0 L 336 2">
			</path>
		</svg>
		<!-- 日曆放這邊 -->

		<div id="calendar"></div>
		<script src="../js/video.js"></script>
		<script type="text/javascript">
		//js呼叫php變數
		var userCount ="<?php echo $count; ?>" ; //賦值
		var userSport1 =<?php echo json_encode($arraySport1); ?> ; //賦值
		var userSport2 =<?php echo json_encode($arraySport2); ?> ; //賦值
		var userSport3 =<?php echo json_encode($arraySport3); ?> ; //賦值
		var userSport4 =<?php echo json_encode($arraySport4); ?> ; //賦值
		var userDate =<?php echo json_encode($arrayDate); ?> ; //賦值
		var userid =<?php echo json_encode($id); ?> ; //賦值
		
		//alert(userid);
		!function() {
			var data = [];
			for(i=0;i<userCount;i++){
				if(userSport1[i] != 0){
					data.push({
						eventName : "舉啞鈴 : "+userSport1[i],
						calendar : '舉啞鈴',
						color : 'orange',
						date : userDate[i]
					});
				}
				if(userSport2[i] != 0){
					data.push({
						eventName : "深蹲 : "+userSport2[i],
						calendar : '深蹲',
						color : 'blue',
						date : userDate[i]
					});
				}
				if(userSport3[i] != 0){
					data.push({
						eventName : "伏地挺身 : "+userSport3[i],
						calendar : '伏地挺身',
						color : 'green',
						date : userDate[i]
					});
				}
				if(userSport4[i] != 0){
					data.push({
						eventName : "步數 : "+userSport4[i],
						calendar : '步數',
						color : 'orange',
						date : userDate[i]
					});
				}
			}

			// var data = [
			//     { eventName: "做了"+userSport1[2]+"下深蹲", calendar: 'Squat', color: 'orange' ,date:userDate[2]},
			//     { eventName: "做了"+userSport2[2]+"下挺舉", calendar: 'Deadlifts', color: 'blue' ,date:userDate[2]},
			//     { eventName: "做了"+userSport3[2]+"下臥舉", calendar: 'clean and jerk', color: 'green',date:userDate[2]}
			// ];
		function addDate(ev) {
		}

		var calendar = new Calendar('#calendar', data);
		}();

		</script>
		<div id="functionbar" >
			<!-- functionbar box -->
			<div id="wdraw">

			</div>
			<!-- functionbar line -->
			<svg class="_49_d" viewBox="0 0 375 1">
				<path id="_49_d" d="M 0 0 L 375 0">
				</path>
			</svg>
			<div id="_53_d">
				<a href="HSA.php">
					<div id="clipboard-data_d">
						<svg class="_10_d" viewBox="2.25 3.375 26.586 26.337">
							<path id="_10_d" d="M 7.947022914886475 3.374999761581421 L 6.048015594482422 3.374999761581421 C 3.95042896270752 3.374999761581421 2.249999523162842 5.001402378082275 2.25 7.007670402526855 L 2.25 26.07918739318848 C 2.25 28.08545684814453 3.950428485870361 29.71185684204102 6.048014640808105 29.71185684204102 L 25.03808784484863 29.71185684204102 C 27.13567161560059 29.71185684204102 28.83610343933105 28.08545684814453 28.83610343933105 26.07918739318848 L 28.83610343933105 7.007670402526855 C 28.83610343933105 5.001401901245117 27.13567161560059 3.374999761581421 25.03808784484863 3.374999761581421 L 23.13908004760742 3.374999761581421 L 23.13908004760742 5.191335678100586 L 25.03808784484863 5.191335678100586 C 26.08688163757324 5.191335678100586 26.93709754943848 6.004535675048828 26.93709754943848 7.007670402526855 L 26.93709754943848 26.07918739318848 C 26.93709754943848 27.08231925964355 26.08688163757324 27.89552116394043 25.03808784484863 27.89552116394043 L 6.048015594482422 27.89552116394043 C 4.999222278594971 27.89552116394043 4.149007320404053 27.08231925964355 4.149007320404053 26.07918739318848 L 4.149007320404053 7.007670402526855 C 4.149007320404053 6.004535675048828 4.999222278594971 5.191335678100586 6.048015594482422 5.191335678100586 L 7.947022914886475 5.191335678100586 L 7.947022914886475 3.374999761581421 Z">
							</path>
						</svg>
						<svg class="_11_d" viewBox="11.25 0 8.973 5.982">
							<path id="_11_d" d="M 17.9796085357666 1.495468378067017 L 13.49320220947266 1.495468378067017 C 13.08024024963379 1.495468378067017 12.74546813964844 1.830240368843079 12.74546813964844 2.243202686309814 L 12.74546813964844 3.738670825958252 C 12.74546813964844 4.151632785797119 13.08024024963379 4.486404895782471 13.49320220947266 4.486404895782471 L 17.9796085357666 4.486404895782471 C 18.39257049560547 4.486404895782471 18.72734260559082 4.151632785797119 18.72734260559082 3.738670825958252 L 18.72734260559082 2.243202447891235 C 18.72734260559082 1.830240368843079 18.39257049560547 1.495468378067017 17.9796085357666 1.495468378067017 Z M 13.49320220947266 0 C 12.25431632995605 0 11.25 1.004316329956055 11.25000095367432 2.243202686309814 L 11.25 3.738670825958252 C 11.25000095367432 4.97755765914917 12.25431728363037 5.981873989105225 13.49320411682129 5.981873512268066 L 17.9796085357666 5.981873512268066 C 19.2184944152832 5.981873512268066 20.22281074523926 4.97755765914917 20.22281074523926 3.738670587539673 L 20.22281074523926 2.243202447891235 C 20.22281074523926 1.004315853118896 19.2184944152832 0 17.9796085357666 0 L 13.49320220947266 0 Z">
							</path>
						</svg>
						<svg class="_12_d" viewBox="9 13.5 17.613 10.468">
							<path id="_12_d" d="M 8.999999046325684 20.97734069824219 C 8.999999046325684 20.15141677856445 9.9857177734375 19.48187255859375 11.20166110992432 19.48187255859375 C 12.41760635375977 19.48187255859375 13.40332317352295 20.15141677856445 13.40332317352295 20.97734069824219 L 13.40332317352295 22.47280883789062 C 13.40332317352295 23.29873657226562 12.41760635375977 23.96827697753906 11.20166110992432 23.96827697753906 C 9.9857177734375 23.96827697753906 8.999999046325684 23.29873657226562 8.999999046325684 22.47280883789062 L 8.999999046325684 20.97734069824219 Z M 22.2099723815918 14.99546813964844 C 22.2099723815918 14.1695442199707 23.1956901550293 13.5 24.4116325378418 13.5 C 25.62757873535156 13.5 26.61329650878906 14.1695442199707 26.61329650878906 14.99546813964844 L 26.61329650878906 22.47280883789062 C 26.61329650878906 23.29873657226562 25.62757873535156 23.96827697753906 24.4116325378418 23.96827697753906 C 23.19568634033203 23.96827697753906 22.2099723815918 23.29873657226562 22.2099723815918 22.47280883789062 L 22.2099723815918 14.99546813964844 Z M 15.60498332977295 17.98640441894531 C 15.60498332977295 17.16048049926758 16.5907039642334 16.49093627929688 17.8066463470459 16.49093627929688 C 19.02259063720703 16.49093627929688 20.0083122253418 17.16048049926758 20.0083122253418 17.98640441894531 L 20.0083122253418 22.47280883789062 C 20.0083122253418 23.29873657226562 19.02259063720703 23.96827697753906 17.8066463470459 23.96827697753906 C 16.59070205688477 23.96827697753906 15.60498332977295 23.29873657226562 15.60498332977295 22.47280883789062 L 15.60498332977295 17.98640441894531 Z">
							</path>
						</svg>
					</div>
				</a>
				<a href="SET.php">
					<div id="gear_d">
						<svg class="_3_d" viewBox="0.002 0.001 29.68 31.906">
							<path id="_3_d" d="M 16.3945140838623 3.242441415786743 C 15.9385461807251 1.576944589614868 13.74528789520264 1.576944589614868 13.2893180847168 3.242441415786743 L 13.11534118652344 3.878857612609863 C 12.81847095489502 4.961498737335205 12.08211517333984 5.841769218444824 11.11207008361816 6.273659229278564 C 10.14202499389648 6.705548763275146 9.042327880859375 6.642733097076416 8.120317459106445 6.102770805358887 L 7.578597545623779 5.783675670623779 C 6.161224365234375 4.955802440643311 4.610275745391846 6.621299743652344 5.382039070129395 8.146748542785645 L 5.677222728729248 8.729096412658691 C 6.179198741912842 9.720182418823242 6.237457752227783 10.90210342407227 5.835724830627441 11.94466781616211 C 5.4339919090271 12.98723411560059 4.615335941314697 13.77866458892822 3.608466863632202 14.09786605834961 L 3.016451835632324 14.28488636016846 C 1.467152237892151 14.77505207061768 1.467152237892151 17.1328067779541 3.016451835632324 17.62297439575195 L 3.608466863632202 17.80999755859375 C 4.6158127784729 18.12907791137695 5.434870719909668 18.92080688476562 5.836653232574463 19.96384048461914 C 6.238436222076416 21.00687980651855 6.179830551147461 22.18930435180664 5.677222728729248 23.18054008483887 L 5.38038969039917 23.7611141204834 C 4.610275268554688 25.2847957611084 6.159574508666992 26.95206451416016 7.578597068786621 26.12241363525391 L 8.120316505432129 25.80509567260742 C 9.04248046875 25.26551246643066 10.14215660095215 25.20312309265137 11.11203193664551 25.63535118103027 C 12.08190727233887 26.06758117675781 12.81796836853027 26.94807624816895 13.11451816558838 28.0307788848877 L 13.28849315643311 28.66542053222656 C 13.744460105896 30.33092308044434 15.93772029876709 30.33092308044434 16.3936882019043 28.66542053222656 L 16.56766510009766 28.02900314331055 C 16.86448097229004 26.94610786437988 17.60097312927246 26.06561470031738 18.57124137878418 25.63370513916016 C 19.54150772094727 25.20178413391113 20.64143943786621 25.2647876739502 21.56351852416992 25.80509376525879 L 22.10358619689941 26.12418937683105 C 23.52096366882324 26.95206260681152 25.07191467285156 25.28656387329102 24.30014991760254 23.7611141204834 L 24.00496292114258 23.18053436279297 C 23.50239753723145 22.18906402587891 23.44401168823242 21.00641059875488 23.84613609313965 19.96331977844238 C 24.24825668334961 18.92023086547852 25.06772613525391 18.12866592407227 26.07536697387695 17.80999755859375 L 26.66573143005371 17.62297248840332 C 28.21503448486328 17.1328067779541 28.21503448486328 14.77505207061768 26.66573143005371 14.28488540649414 L 26.0737190246582 14.09786224365234 C 25.06684875488281 13.77866363525391 24.24819183349609 12.98723125457764 23.84646034240723 11.94466495513916 C 23.44472885131836 10.90210151672363 23.50298309326172 9.720179557800293 24.00496292114258 8.729092597961426 L 24.30179786682129 8.146745681762695 C 25.07191276550293 6.623069763183594 23.52260971069336 4.95580005645752 22.10358619689941 5.785444736480713 L 21.56351470947266 6.102767467498779 C 20.64143180847168 6.643070220947266 19.54150772094727 6.706071853637695 18.57124137878418 6.274157524108887 C 17.60097312927246 5.842241287231445 16.86448097229004 4.96175479888916 16.56766319274902 3.87885856628418 L 16.3936882019043 3.242441415786743 Z M 11.50997638702393 2.677820920944214 C 12.48787307739258 -0.8916069269180298 17.19596099853516 -0.8916069269180298 18.17385864257812 2.677820920944214 L 18.34783554077148 3.314237356185913 C 18.48604202270508 3.819069147109985 18.82926368713379 4.229598522186279 19.28150939941406 4.431020259857178 C 19.73375701904297 4.632441997528076 20.24649238586426 4.603135585784912 20.67632102966309 4.351294994354248 L 21.2180347442627 4.032200336456299 C 24.26057434082031 2.253247499465942 27.58921051025391 5.82888126373291 25.93025016784668 9.099599838256836 L 25.63506698608398 9.681947708129883 C 25.40080070495605 10.14401340484619 25.37353897094727 10.6952018737793 25.56090927124023 11.18136787414551 C 25.7482738494873 11.66753482818604 26.13016128540039 12.0364933013916 26.59977531433105 12.18506908416748 L 27.1917839050293 12.37209510803223 C 30.51218414306641 13.4233341217041 30.51218414306641 18.48452758789062 27.1917839050293 19.53576850891113 L 26.59977149963379 19.72279357910156 C 26.13016128540039 19.87137031555176 25.7482738494873 20.24033164978027 25.56090354919434 20.72649383544922 C 25.37353706359863 21.21265983581543 25.40079879760742 21.76384925842285 25.63506698608398 22.22591590881348 L 25.93190002441406 22.80826187133789 C 27.58838653564453 26.0789852142334 24.25809478759766 29.65727233886719 21.2180347442627 27.8738899230957 L 20.67631530761719 27.55657005310059 C 20.24648857116699 27.30472755432129 19.73375511169434 27.27542114257812 19.28150749206543 27.47684288024902 C 18.82925987243652 27.67826461791992 18.48604011535645 28.08880043029785 18.34783363342285 28.5936222076416 L 18.17385292053223 29.23004150390625 C 17.19595909118652 32.79946899414062 12.48787117004395 32.79946899414062 11.50997638702393 29.23004150390625 L 11.33599758148193 28.5936222076416 C 11.19779014587402 28.08880043029785 10.85457324981689 27.67826461791992 10.40232467651367 27.47684288024902 C 9.950077056884766 27.27542114257812 9.437344551086426 27.30472755432129 9.007513999938965 27.55657005310059 L 8.465795516967773 27.87565994262695 C 5.423264980316162 29.65638542175293 2.097095251083374 26.07632446289062 3.753583669662476 22.80826187133789 L 4.048766613006592 22.22591209411621 C 4.283035755157471 21.76384544372559 4.310298442840576 21.21265983581543 4.122929096221924 20.72649383544922 C 3.935560464859009 20.24032592773438 3.553672075271606 19.87136840820312 3.084062814712524 19.72279357910156 L 2.49204683303833 19.5357666015625 C -0.8283514380455017 18.48452758789062 -0.8283514380455017 13.42333221435547 2.49204683303833 12.37209320068359 L 3.084062099456787 12.18506622314453 C 3.553672075271606 12.0364933013916 3.935560464859009 11.66753482818604 4.122929573059082 11.18136692047119 C 4.310298442840576 10.69520092010498 4.283035755157471 10.14401149749756 4.048766613006592 9.681946754455566 L 3.751934289932251 9.099599838256836 C 2.097094774246216 5.828879356384277 5.425737857818604 2.253246784210205 8.465795516967773 4.033971786499023 L 9.007513999938965 4.351294040679932 C 9.437344551086426 4.603133678436279 9.950077056884766 4.632441520690918 10.40232467651367 4.431018829345703 C 10.85457324981689 4.229598045349121 11.19779205322266 3.81906795501709 11.33599853515625 3.314236640930176 L 11.50997543334961 2.67781925201416 Z">
							</path>
						</svg>
						<svg class="_4_d" viewBox="10.696 10.696 10.839 10.839">
							<path id="_4_d" d="M 16.11562919616699 12.365647315979 C 14.04470443725586 12.36564540863037 12.36588859558105 14.04446220397949 12.36588859558105 16.11538696289062 C 12.36588859558105 18.18631172180176 14.04470443725586 19.86512756347656 16.11562919616699 19.86512756347656 C 18.18655395507812 19.86512756347656 19.86536979675293 18.18631172180176 19.86536979675293 16.11538887023926 C 19.86536979675293 14.04446411132812 18.18655395507812 12.36564922332764 16.11562919616699 12.36564922332764 Z M 10.69599914550781 16.11575889587402 C 10.69600105285645 13.12278461456299 13.12228584289551 10.69649982452393 16.11526107788086 10.69649982452393 C 19.10823440551758 10.69649982452393 21.53451919555664 13.1227855682373 21.53451919555664 16.11576080322266 C 21.53451919555664 19.10873413085938 19.10823440551758 21.53502082824707 16.11526107788086 21.53502082824707 C 13.12228584289551 21.53502082824707 10.69600105285645 19.10873413085938 10.69600105285645 16.11576080322266 Z">
							</path>
						</svg>
					</div>
				</a>	
				<a href="tool.php">
				<img id="gym_d" src="../picture/gym.png" srcset="../picture/gym.png 1x, ../picture/gym@2x.png 2x">
				</a>
				<a href="HM.php">
					<div id="house-door_ea">
						<svg class="_32_eb" viewBox="3.375 2.248 26.586 28.58">
							<path id="_32_eb" d="M 15.94406509399414 2.548348665237427 C 16.13590812683105 2.356377840042114 16.39639663696289 2.248488903045654 16.66805076599121 2.248488664627075 C 16.93970489501953 2.248488664627075 17.20019340515137 2.356377840042114 17.39203834533691 2.548348665237427 L 29.66296195983887 14.79636001586914 C 29.85434532165527 14.9881067276001 29.96158599853516 15.24787616729736 29.96110343933105 15.5185375213623 L 29.96110153198242 29.80788421630859 C 29.96110343933105 30.37158393859863 29.5032787322998 30.82855224609375 28.93852424621582 30.82855224609375 L 19.73623657226562 30.82855224609375 C 19.17148399353027 30.82855224609375 18.71366119384766 30.37158393859863 18.71366119384766 29.80788421630859 L 18.71366119384766 21.64254379272461 L 14.62335014343262 21.64254379272461 L 14.62335014343262 29.80788421630859 C 14.62335014343262 30.37158393859863 14.16552639007568 30.82855224609375 13.60077285766602 30.82855224609375 L 4.397577285766602 30.82855224609375 C 3.832823276519775 30.82855224609375 3.374999523162842 30.37158393859863 3.374999523162842 29.80788421630859 L 3.374999523162842 15.5185375213623 C 3.374515056610107 15.24787616729736 3.481757164001465 14.9881067276001 3.67313814163208 14.79636001586914 L 15.94406509399414 2.548349142074585 Z M 5.420154571533203 15.94131946563721 L 5.420154571533203 28.78721809387207 L 12.57819557189941 28.78721809387207 L 12.57819557189941 20.62187576293945 C 12.57819557189941 20.05817604064941 13.03602027893066 19.6012077331543 13.60077285766602 19.6012077331543 L 19.73623657226562 19.6012077331543 C 20.30099296569824 19.6012077331543 20.75881576538086 20.05817604064941 20.75881576538086 20.62187576293945 L 20.75881576538086 28.78721809387207 L 27.9168586730957 28.78721809387207 L 27.9168586730957 15.94131946563721 L 16.66850471496582 4.713978290557861 L 5.420154571533203 15.94131946563721 Z">
							</path>
						</svg>
						<svg class="_33_ec" viewBox="24.75 4.5 2.991 5.982">
							<path id="_33_ec" d="M 27.74093627929688 5.247734069824219 L 27.74093627929688 10.48187351226807 L 24.75 7.490937232971191 L 24.75 5.247734069824219 C 24.75 4.834772109985352 25.08477210998535 4.5 25.49773406982422 4.5 L 26.99320220947266 4.5 C 27.40616416931152 4.5 27.74093627929688 4.834772109985352 27.74093627929688 5.247734069824219 Z">
							</path>
						</svg>
					</div>
				</a>
				<a href="HR.php">
					<div  id="calendar-week_ed">
						<svg class="_46_ee" viewBox="0 2.25 26.586 27.117">
							<path id="draw" d="M 1.661632537841797 7.673345565795898 L 1.661632537841797 25.75116729736328 C 1.661632537841797 26.74957656860352 2.405570268630981 27.5589485168457 3.323264360427856 27.5589485168457 L 23.26285552978516 27.5589485168457 C 24.18054962158203 27.5589485168457 24.92448806762695 26.74957656860352 24.92448806762695 25.75116729736328 L 24.92448806762695 7.673345565795898 L 1.661632537841797 7.673345565795898 Z M 3.323265075683594 2.249999761581421 C 1.487876296043396 2.249999761581421 -3.521458040722791e-07 3.868742942810059 0 5.865564346313477 L 0 25.75116729736328 C 0 27.74798583984375 1.487876057624817 29.36672782897949 3.323264360427856 29.36672782897949 L 23.26285552978516 29.36672782897949 C 25.09824180603027 29.36672782897949 26.58612060546875 27.74798583984375 26.58612060546875 25.75116729736328 L 26.58612060546875 5.86556339263916 C 26.58612060546875 3.8687424659729 25.09824180603027 2.249999761581421 23.26285552978516 2.249999761581421 L 3.323265075683594 2.249999761581421 Z">
							</path>
						</svg>
						<svg class="_47_ef" viewBox="6.75 0 17.806 2.195">
							<path id="draw" d="M 7.640301704406738 0 C 8.132000923156738 0 8.530603408813477 0.3275817036628723 8.530603408813477 0.7316741943359375 L 8.530603408813477 1.463348388671875 C 8.530603408813477 1.867440700531006 8.132000923156738 2.195022583007812 7.640301704406738 2.195022583007812 C 7.148601055145264 2.195022583007812 6.750000476837158 1.867440700531006 6.750000476837158 1.463348388671875 L 6.750000476837158 0.7316741943359375 C 6.750000476837158 0.3275816738605499 7.148601055145264 -7.753098429930105e-08 7.640301704406738 0 Z M 23.66573143005371 0 C 24.15742874145508 0 24.55603218078613 0.3275817036628723 24.55603218078613 0.7316741943359375 L 24.55603218078613 1.463348388671875 C 24.55603218078613 1.867440700531006 24.15742874145508 2.195022583007812 23.66573143005371 2.195022583007812 C 23.17403030395508 2.195022583007812 22.77542877197266 1.867440700531006 22.77542877197266 1.463348388671875 L 22.77542877197266 0.7316741943359375 C 22.77542877197266 0.3275816738605499 23.17403030395508 -7.753098429930105e-08 23.66573143005371 0 Z">
							</path>
						</svg>
						<svg class="_46_e" viewBox="0 2.25 26.586 27.117">
							<path id="wdraw" d="M 1.661632537841797 7.673345565795898 L 1.661632537841797 25.75116729736328 C 1.661632537841797 26.74957656860352 2.405570268630981 27.5589485168457 3.323264360427856 27.5589485168457 L 23.26285552978516 27.5589485168457 C 24.18054962158203 27.5589485168457 24.92448806762695 26.74957656860352 24.92448806762695 25.75116729736328 L 24.92448806762695 7.673345565795898 L 1.661632537841797 7.673345565795898 Z M 3.323265075683594 2.249999761581421 C 1.487876296043396 2.249999761581421 -3.521458040722791e-07 3.868742942810059 0 5.865564346313477 L 0 25.75116729736328 C 0 27.74798583984375 1.487876057624817 29.36672782897949 3.323264360427856 29.36672782897949 L 23.26285552978516 29.36672782897949 C 25.09824180603027 29.36672782897949 26.58612060546875 27.74798583984375 26.58612060546875 25.75116729736328 L 26.58612060546875 5.86556339263916 C 26.58612060546875 3.8687424659729 25.09824180603027 2.249999761581421 23.26285552978516 2.249999761581421 L 3.323265075683594 2.249999761581421 Z">
							</path>
						</svg>
						<svg class="_48_eg" viewBox="6.75 13.5 17.806 7.317">
							<path id="draw" d="M 20.99482536315918 14.23167419433594 C 20.99482536315918 13.82758140563965 21.39342498779297 13.5 21.88512802124023 13.5 L 23.66573143005371 13.5 C 24.15742874145508 13.5 24.55603218078613 13.82758140563965 24.55603218078613 14.23167419433594 L 24.55603218078613 15.69502258300781 C 24.55603218078613 16.09911346435547 24.15742874145508 16.42669677734375 23.66573143005371 16.42669677734375 L 21.88512802124023 16.42669677734375 C 21.39342498779297 16.42669677734375 20.99482536315918 16.09911346435547 20.99482536315918 15.69502258300781 L 20.99482536315918 14.23167419433594 Z M 15.65301609039307 14.23167419433594 C 15.65301609039307 13.82758140563965 16.05161666870117 13.5 16.54331588745117 13.5 L 18.32392120361328 13.5 C 18.81561851501465 13.5 19.2142219543457 13.82758140563965 19.2142219543457 14.23167419433594 L 19.2142219543457 15.69502258300781 C 19.2142219543457 16.09911346435547 18.81561851501465 16.42669677734375 18.32392120361328 16.42669677734375 L 16.54331588745117 16.42669677734375 C 16.05161666870117 16.42669677734375 15.65301609039307 16.09911346435547 15.65301609039307 15.69502258300781 L 15.65301609039307 14.23167419433594 Z M 6.750000476837158 18.62171936035156 C 6.750000476837158 18.21762466430664 7.148601055145264 17.89004516601562 7.640301704406738 17.89004516601562 L 9.420905113220215 17.89004516601562 C 9.912605285644531 17.89004516601562 10.31120681762695 18.21762466430664 10.31120681762695 18.62171936035156 L 10.31120681762695 20.08506774902344 C 10.31120681762695 20.48915863037109 9.912605285644531 20.81674194335938 9.420905113220215 20.81674194335938 L 7.640301704406738 20.81674194335938 C 7.148601055145264 20.81674194335938 6.750000476837158 20.48915863037109 6.750000476837158 20.08506774902344 L 6.750000476837158 18.62171936035156 Z M 12.09180927276611 18.62171936035156 C 12.09180927276611 18.21762466430664 12.49041080474854 17.89004516601562 12.98211097717285 17.89004516601562 L 14.76271438598633 17.89004516601562 C 15.25441360473633 17.89004516601562 15.65301609039307 18.21762466430664 15.65301609039307 18.62171936035156 L 15.65301609039307 20.08506774902344 C 15.65301609039307 20.48915863037109 15.25441360473633 20.81674194335938 14.76271438598633 20.81674194335938 L 12.98211097717285 20.81674194335938 C 12.49041080474854 20.81674194335938 12.09180927276611 20.48915863037109 12.09180927276611 20.08506774902344 L 12.09180927276611 18.62171936035156 Z">
							</path>
						</svg>
					</div>
				</a>
			</div>
		</div>
	</div>
</div>
</body>
</html>
<?php
    //釋放資源及關閉資料連接
    sqlsrv_free_stmt($result);
    sqlsrv_close($link);
}
?>