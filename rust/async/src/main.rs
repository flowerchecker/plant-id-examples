use rustc_serialize::base64::{ToBase64, MIME};
use rustc_serialize::hex::{ToHex};
use std::path::Path;
use std::fs::File;
use std::io::Read;
use regex::Regex;
use serde_json::{Value};

#[tokio::main]
async fn main() {
    // Read image and convert to hex
    let path = Path::new("../images/photo1.jpg");
    let mut file = File::open(&path).unwrap();
    let mut buffer = Vec::new();
    let _out = file.read_to_end(&mut buffer);
    let b64 = buffer.to_base64(MIME);
    let hex = buffer.to_hex();

    // Convert hex to base64
    let base64img = format!("data:image/{};base64,{}", get_type(&hex), b64);

    // Perform request
    let echo_json = reqwest::Client::new()
        .post("https://api.plant.id/v2/identify")
        .json(&serde_json::json!({
            "api_key": "-- ask for one: https://web.plant.id/api-access-request/ --",
            "images": [base64img],
            // modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
            "modifiers": ["crops_fast", "similar_images"],
            "plant_language": "en",
            // plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
            "plant_details": ["common_names",
                "url",
                "name_authority",
                "wiki_description",
                "taxonomy",
                "synonyms"],
        }))
        .send()
        .await;
        

    // Process response
    if let Ok(response) = echo_json {
        if let Ok(text) = response.text().await {
            let result: serde_json::Result<Value> = serde_json::from_str(&text);
            if let Ok(data) = result {
                println!("{}", data);
            } else {
                println!("{}", text);
            }
        }
    }
}

// Returns file extension (needed for creating the base64 string)
fn get_type(file: &str) -> &str {
    if Regex::new(r"^ffd8ffe0").unwrap().is_match(file) { "jpg" }
    else if Regex::new(r"^89504e47").unwrap().is_match(file){ "png" }
    else if Regex::new(r"^47494638").unwrap().is_match(file){ "gif" }
    else { panic!("invalid file") }
  }
