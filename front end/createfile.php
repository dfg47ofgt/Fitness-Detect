<<<<<<< HEAD
<?php
//資料夾的建立
$filename="2";

$file_path = "C:/inetpub/wwwroot/video/$filename/";
if(!file_exists($file_path)){
 mkdir($file_path);
 echo "建立資料夾成功";
}else{
 echo "資料夾已存在";
}
=======
<?php
//資料夾的建立
$filename="2";

$file_path = "C:/inetpub/wwwroot/video/$filename/";
if(!file_exists($file_path)){
 mkdir($file_path);
 echo "建立資料夾成功";
}else{
 echo "資料夾已存在";
}
>>>>>>> origin/main
?>