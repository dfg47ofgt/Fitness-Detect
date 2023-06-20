<<<<<<< HEAD
<?php
  function create_connection()
  {
    // $serverName = "DESKTOP-F1LL06A\SQLEXPRESS"; 
    // $link = mysqli_connect("localhost", "root", "abc12345")
    // $conn = sqlsrv_connect( $serverName, $connectionInfo);
    $connectionInfo = array( "Database"=>"graduation_project", "UID"=>"fitness", "PWD"=>"abc12345" , "CharacterSet"=>"UTF-8");
    // $link = sqlsrv_connect("localhost", $connectionInfo)
    $link = sqlsrv_connect("172.22.248.10,9999", $connectionInfo)
    
    //   or die("無法建立資料連接: " . mysqli_connect_error());
    or die("無法建立資料連接: " .print_r(sqlsrv_errors()) );
	  
    // mysqli_query($link, "SET NAMES utf8");
    sqlsrv_query($link, "SET NAMES utf8");
			   	
    return $link;
  }
	
  function execute_sql($link, $sql, $database)
  {
    sqlsrv_prepare($link, $database)
      or die("開啟資料庫失敗: " . sqlsrv_errors($link));
						 
    $result = sqlsrv_query($link, $sql);
		
    return $result;
  }
?>
=======
<?php
  function create_connection()
  {
    // $serverName = "DESKTOP-F1LL06A\SQLEXPRESS"; 
    // $link = mysqli_connect("localhost", "root", "abc12345")
    // $conn = sqlsrv_connect( $serverName, $connectionInfo);
    $connectionInfo = array( "Database"=>"graduation_project", "UID"=>"fitness", "PWD"=>"abc12345" , "CharacterSet"=>"UTF-8");
    // $link = sqlsrv_connect("localhost", $connectionInfo)
    $link = sqlsrv_connect("172.22.248.10,9999", $connectionInfo)
    
    //   or die("無法建立資料連接: " . mysqli_connect_error());
    or die("無法建立資料連接: " .print_r(sqlsrv_errors()) );
	  
    // mysqli_query($link, "SET NAMES utf8");
    sqlsrv_query($link, "SET NAMES utf8");
			   	
    return $link;
  }
	
  function execute_sql($link, $sql, $database)
  {
    sqlsrv_prepare($link, $database)
      or die("開啟資料庫失敗: " . sqlsrv_errors($link));
						 
    $result = sqlsrv_query($link, $sql);
		
    return $result;
  }
?>
>>>>>>> origin/main
