require 'uri'
require 'net/http'
require 'json'

api_key = "YOUR_KEY_HERE"
base64_image = "YOUR_BASE64_STRING_HERE"
images = [base64_image]
modifiers = ["crops_fast", "similar_images"]
plant_language = "en"
plant_details = ["common_names", "url", "name_authority", "wiki_description", "taxonomy", "synonyms"]

uri = URI('https://api.plant.id/v2/identify')
https = Net::HTTP.new(uri.host, uri.port)
https.use_ssl = true

request = Net::HTTP::Post.new(uri.path)

data = {
  "images": images,
  "modifiers": modifiers,
  "plant_details": plant_details,
  "api_key": api_key
}.to_json
request.body = data

# API key can be pass either in the body or as a headers
# request["Api-Key"] = api_key
request["Content-Type"] = "application/json"
response = https.request(request)
json_raw =  response.body
p JSON.parse(json_raw)
