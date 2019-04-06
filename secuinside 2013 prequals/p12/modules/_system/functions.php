<?php
 if(!defined('__BHACK__')) exit();

 function db_conn(){
 	global $_BHVAR;
	mysql_connect($_BHVAR['db']['host'], $_BHVAR['db']['user'], $_BHVAR['db']['pass']);
	mysql_select_db($_BHVAR['db']['name']);
 }

 function get_layout($layout, $pos){
	$result = mysql_query("select path from _BH_layout where layout_name='$layout' and position='$pos'");
	$row = mysql_fetch_array($result);
	if (!isset($row['path'])){
		if ($pos = 'head'){
			return "./reverted/h.htm";
		} else {
			return "./reverted/f.htm";
		}
	}
	return $row['path'];
 }

 function filtering($str){
 	$str = preg_replace("/select/","", $str);
 	$str = preg_replace("/union/","", $str);
 	$str = preg_replace("/from/","", $str);
 	$str = preg_replace("/load_file/","", $str);
 	$str = preg_replace("/ /","", $str);
 	return $str;
 }


?>