import Foundation

/// Encode an image file into Base64 ASCII
func encodeFile(_ url: URL) -> String? {
    do {
        let data = try Data(contentsOf: url)
        return data.base64EncodedString()
    } catch {
        return nil
    }
}

/// Identify a plant given a list of file URLs
func identifyPlant(from files: [URL]) async -> String? {
    let paramaters: [String: Any] = [
        "api_key": "-- ask for one: https://web.plant.id/api-access-request/ --",
        "images": files.compactMap(encodeFile),
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "datetime": 1582830233,
        // modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
        "modifiers": ["crops_fast", "similar_images", "health_all", "disease_similar_images"],
        "plant_language": "en",
        // plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
        "plant_details": ["common_names",
                          "edible_parts",
                          "gbif_id",
                          "name_authority",
                          "propagation_methods",
                          "synonyms",
                          "taxonomy",
                          "url",
                          "wiki_description",
                          "wiki_image",
        ],
        // disease details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Disease-details
        "disease_details": ["common_names", "url", "description"]
    ]
    
    let url = URL(string: "https://api.plant.id/v2/identify")!
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.addValue("application/json", forHTTPHeaderField:  "Content-Type")
    request.httpBody = try! JSONSerialization.data(withJSONObject: paramaters)
    
    let task = try! await URLSession.shared.data(for: request)
    return String(data: task.0, encoding: .utf8)
}

/// Perform a plant identification request using some sample images
func performRequest() {
    Task {
        let urls = [
            Bundle.main.url(forResource: "photo1", withExtension: "jpg")!,
            Bundle.main.url(forResource: "photo2", withExtension: "jpg")!,
            Bundle.main.url(forResource: "photo3", withExtension: "jpg")!
        ]
        if let response = await identifyPlant(from: urls) {
            print(response)
        }
    }
}
