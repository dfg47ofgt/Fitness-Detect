<<<<<<< HEAD
<?php
  require_once("dbtools.inc.php");
  
  //取得表單資料
  $account = $_POST["account"];
  $password = $_POST["password"]; 
  $first_name = $_POST["first_name"]; 
  $last_name = $_POST["last_name"]; 
  $sex = $_POST["sex"];
  $date = $_POST["date"]; 

  //建立資料連接
  $link = create_connection();
	
  //檢查帳號是否有人申請
  $sql = "SELECT * FROM users Where account = '$account'";
  $result = execute_sql($link, $sql, "graduation_project");

  //如果帳號已經有人使用
  if (sqlsrv_has_rows($result) != 0)
  {
    //釋放 $result 佔用的記憶體
    sqlsrv_free_stmt($result);
    
    //顯示訊息要求使用者更換帳號名稱
    echo "<script type='text/javascript'>";
    echo "alert('您所指定的帳號已經有人使用，請使用其它帳號');";
    echo "history.back();";
    echo "</script>";
  }
	
  //如果帳號沒人使用
  else
  {
    //釋放 $result 佔用的記憶體	
    sqlsrv_free_stmt($result);
		
    //執行 SQL 命令，新增此帳號
    $sql = "INSERT INTO users (account, password, first_name, last_name, date, sex) 
            VALUES ('$account', '$password', '$first_name', '$last_name', '$date', '$sex')";
    $result = execute_sql($link, $sql, "graduation_project");

    //關閉資料連接	
    sqlsrv_close($link);
    header("location:../html/login.php");
  }   
=======
<?php
  require_once("dbtools.inc.php");
  
  //取得表單資料
  $account = $_POST["account"];
  $password = $_POST["password"]; 
  $first_name = $_POST["first_name"]; 
  $last_name = $_POST["last_name"]; 
  $sex = $_POST["sex"];
  $date = $_POST["date"]; 

  //建立資料連接
  $link = create_connection();
	
  //檢查帳號是否有人申請
  $sql = "SELECT * FROM users Where account = '$account'";
  $result = execute_sql($link, $sql, "graduation_project");

  //如果帳號已經有人使用
  if (sqlsrv_has_rows($result) != 0)
  {
    //釋放 $result 佔用的記憶體
    sqlsrv_free_stmt($result);
    
    //顯示訊息要求使用者更換帳號名稱
    echo "<script type='text/javascript'>";
    echo "alert('您所指定的帳號已經有人使用，請使用其它帳號');";
    echo "history.back();";
    echo "</script>";
  }
	
  //如果帳號沒人使用
  else
  {
    //釋放 $result 佔用的記憶體	
    sqlsrv_free_stmt($result);
		
    //執行 SQL 命令，新增此帳號
    $sql = "INSERT INTO users (account, password, first_name, last_name, date, sex) 
            VALUES ('$account', '$password', '$first_name', '$last_name', '$date', '$sex')";
    $result = execute_sql($link, $sql, "graduation_project");

    //關閉資料連接	
    sqlsrv_close($link);
    header("location:../html/login.php");
  }   
>>>>>>> origin/main
?>