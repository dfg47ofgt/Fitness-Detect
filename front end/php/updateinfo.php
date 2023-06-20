<<<<<<< HEAD
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
  /* 如果 cookie 中的 passed 變數等於 TRUE，
     表示已經登入網站，則取得使用者資料 */
else
{
    require_once("dbtools.inc.php");
	
    //取得 setinfo.php 網頁的表單資料
    $id = $_SESSION['id'];
    $first_name = $_POST["first_name"]; 
    $last_name = $_POST["last_name"]; 
    $sex = $_POST["sex"];
    $height = $_POST["height"];
    $weight = $_POST["weight"];
    $date = $_POST["date"];
    $cellphone = $_POST["cellphone"]; 
    $email = $_POST["email"]; 
    //建立資料連接
    $link = create_connection();
				
    //執行 UPDATE 陳述式來更新使用者資料
      $sql = "UPDATE users SET first_name = '$first_name', last_name = '$last_name', 
            sex = '$sex', height = '$height', weight = '$weight', date = '$date',
            cellphone = '$cellphone', email = '$email' WHERE id = $id";
      $result = execute_sql($link, $sql, "graduation_project");
      // if( $result == false ) {
      //   echo "0";
      // }
      // else{
      //   echo "1";
      // }
    //關閉資料連接	
    sqlsrv_close($link);
    header("location:../html/SET.php");
  }		
=======
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
  /* 如果 cookie 中的 passed 變數等於 TRUE，
     表示已經登入網站，則取得使用者資料 */
else
{
    require_once("dbtools.inc.php");
	
    //取得 setinfo.php 網頁的表單資料
    $id = $_SESSION['id'];
    $first_name = $_POST["first_name"]; 
    $last_name = $_POST["last_name"]; 
    $sex = $_POST["sex"];
    $height = $_POST["height"];
    $weight = $_POST["weight"];
    $date = $_POST["date"];
    $cellphone = $_POST["cellphone"]; 
    $email = $_POST["email"]; 
    //建立資料連接
    $link = create_connection();
				
    //執行 UPDATE 陳述式來更新使用者資料
      $sql = "UPDATE users SET first_name = '$first_name', last_name = '$last_name', 
            sex = '$sex', height = '$height', weight = '$weight', date = '$date',
            cellphone = '$cellphone', email = '$email' WHERE id = $id";
      $result = execute_sql($link, $sql, "graduation_project");
      // if( $result == false ) {
      //   echo "0";
      // }
      // else{
      //   echo "1";
      // }
    //關閉資料連接	
    sqlsrv_close($link);
    header("location:../html/SET.php");
  }		
>>>>>>> origin/main
?>