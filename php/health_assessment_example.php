<?php
function encodeImages($images){
	$encoded_images = array();
	foreach($images as $image){
		$encoded_images[] = base64_encode(file_get_contents($image));
	}
	return $encoded_images;
}
function identifyPlants($file_names){
	$encoded_images = encodeImages($file_names);
	$api_key = "// ask for one: https://web.plant.id/api-access-request/";
	$params = array(
		"api_key" => $api_key,
		"images" => $encoded_images,
		// modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
		"modifiers" => ["crops_fast", "similar_images"],
		"language" => "en",
		// plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
		"disease_details" => array("cause",
							"common_names",
							"classification",
							"description",
							"treatment",
							"url"),
		);
	$params = json_encode($params);
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://api.plant.id/v2/health_assessment");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type:application/json"));
	$result = curl_exec($ch);
	curl_close($ch);
	return $result;
}
print_r(identifyPlants(['../img/photo1.jpg', '../img/photo2.jpg', '../img/photo3.jpg']));
?>