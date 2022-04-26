import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Base64;

import org.json.JSONArray;
import org.json.JSONObject;

public class Sync_Java {
	
	/*
	 *
	 * org.json libraries are required, java standard library can not handle Json.
	 * Maven : https://mvnrepository.com/artifact/org.json/json
	 * Please put this in a package to compile.
	 * 
	*/
	
	private static String base64EncodeFromFile(String fileString) throws Exception {
		File file = new File(fileString);
		FileInputStream fis = new FileInputStream(file);
		String res = Base64.getEncoder().encodeToString(fis.readAllBytes());
		fis.close();
		return res;
	}
	
	public static String sendPostRequest(String urlString, JSONObject data) throws Exception {
		URL url = new URL(urlString);
		HttpURLConnection con = (HttpURLConnection) url.openConnection();

		con.setDoOutput(true);
		con.setDoInput(true);
		con.setRequestMethod("POST");
		con.setRequestProperty("Content-Type", "application/json");

		OutputStream os = con.getOutputStream();
		os.write(data.toString().getBytes());
		os.close();

		InputStream is = con.getInputStream();
		String response = new String(is.readAllBytes());

		System.out.println("Response code : " + con.getResponseCode());
		System.out.println("Response : " + response);
		con.disconnect();
		return response;
	}
	
	public static void main(String[] args) throws Exception {
		
		String apiKey = "// ask for one: https://web.plant.id/api-access-request/";
		
		// read image from local file system and encode
		String [] flowers = new String[] {"../img/photo1.jpg", "../img/photo2.jpg", "../img/photo3.jpg"};
		
		
		JSONObject data = new JSONObject();
		data.put("api_key", apiKey);

		// add images
		JSONArray images = new JSONArray();
		for(String filename : flowers) {
			String fileData = base64EncodeFromFile(filename);
			images.put(fileData);
		}
		data.put("images", images);

		// add modifiers
		// modifiers info: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
		JSONArray modifiers = new JSONArray()
				.put("crops_fast")
				.put("similar_images");
		data.put("modifiers", modifiers);

		// add language
		data.put("plant_language", "en");

		// add plant details
		// more info here: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
		JSONArray plantDetails = new JSONArray()
				.put("common_names")
				.put("url")
				.put("name_authority")
				.put("wiki_description")
				.put("taxonomy")
				.put("synonyms");
		data.put("plant_details", plantDetails);

		sendPostRequest("https://api.plant.id/v2/identify", data);
	}
}