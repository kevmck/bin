#!/usr/bin/php
<?php
require_once('path.inc');
require_once('get_host_info.inc');
require_once('rabbitMQLib.inc');

$client = new rabbitMQClient("testRabbitMQ.ini","testServer");

if( !isset($argv[1]) )
  exit("Need arguments \n");

$request = array();
$request['type'] = $argv[1];
$request['bundle'] = "APIv";
$request['bundleName'] = $argv[2];

switch($argv[1])
{

  case "deployBundle":
  case "rollbackBundle":
	//specify which branch to deploy to
	$request['branch'] = $argv[3];
	break;
}

$response = $client->send_request($request);

print_r($response);

