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
		"modifiers" => ["crops_fast", "similar_images"],
		"plant_language" => "en",
		"plant_details" => array("common_names",
							"url",
							"name_authority",
							"wiki_description",
							"taxonomy",
							"synonyms"),
		);
	$params = json_encode($params);
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://api.plant.id/v2/identify");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type:application/json"));
	$result = curl_exec($ch);
	curl_close($ch);
	return $result;
}
print_r(identifyPlants(['photo1.jpg', 'photo2.jpg']));
?>