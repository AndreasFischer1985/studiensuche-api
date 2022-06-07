<?php

// POST-request:
//--------------
$url = 'https://rest.arbeitsagentur.de/oauth/gettoken_cc';
$data = array(
    'client_id' => '5aee2cfe-1709-48a9-951d-eb48f8f73a74', 
    'client_secret' => '3309a57a-9214-40db-9abe-28b1bb30c08c', 
    'grant_type' => 'client_credentials');
$options = array(
    'http' => array(
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
$tokendata = file_get_contents($url, false, $context);
header('Content-Type: application/json'); 
if(isset($_GET['token']) & $_GET['token']==='TRUE'){
	echo $tokendata;
} else {

    // GET-request:
    //-------------
    $url = 'https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?'.$_SERVER['QUERY_STRING'];
    $options = array(
        'http' => array(
            'header'  => "OAuthAccessToken:".json_decode($tokendata, true)['access_token']." \r\n",
            'method'  => 'GET'    
        )
    );
    $context  = stream_context_create($options);
    $searchdata = file_get_contents($url, false, $context);
    echo $searchdata;
}
?>

