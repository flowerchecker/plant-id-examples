[Plant.id](https://Plant.id) offers a plant identification service based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/), you can use these client's code to speed-up the development of your implementation.

# API reference
## Identification
```https://plant.id/api/identify```

Sends plant photos to our backend, queues the request, and returns its identification.

### Request
There are two required parameters:
- **`key`**- your [API key](https://web.plant.id/plant-identification-api/)
- **`images`** - one ore more images of the plant you want to identify (string - base64 or a file)

The list of optional parameters:
- `custom_id` - identifier you can set for your purpose
<!--- `custom_url` - backlink, your web representation of this identification-->
- `callback_url` - URL where we POST results after identification is completed
- `latitude` - geographic coordinate (float)
- `longitude` - geographic coordinate (float)
- `parameters` - list of strings which specify the speed & accuracy of the identification (`crops_simple`, `crops_fast` - default, `crops_medium`) or allows displaying of similar images (`similar_images`)
- `date` - time in milliseconds (int)
<!--- `week` - week in year (int)-->
<!--- `usage_info` - info about API usage and limits, e. g. how many identifications letf (bool)-->
- `wait_for_identification` - allow to wait some time for identification to finish (and avoid check_identifications call). If the parameter is numerical, it is interpreted as maximal waiting time in seconds (max. 20 s). (bool, float, int)
- `lang` - language code ([ISO 639-1](https://en.m.wikipedia.org/wiki/List_of_ISO_639-1_codes)) used for common names and URLs of plants (default "en")


### Result
The result is a list of records showing possible plant species (taxons). Each record contains:
- `name` - the scientific name of the plant
- `url` - link to Wikipedia or Google
- `common_name` - the common name of the plant
- `probability` - certainty level that suggested plant is the one from the photo
- `confidence` - certainty level of the whole identification
- `similar_images` - representative images of the identified species carefully selected by the model, so it resembles the input image
- `confirmed` - confirmation status

Record example:
```json
{
  "id": 3010636,
  "plant": {
    "name": "Buddleja davidii",
    "url": "https://en.wikipedia.org/wiki/Buddleja_davidii",
    "common_name": "Butterfly-Bush"
  },
  "probability": 0.9277143686644568,
  "confidence": 0.9798141922207031,
  "similar_images": [
    {
      "id": "605775c7cb05e8463f7f8463b0fd915c",
      "similarity": 0.9318117206281141,
      "url": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/605775c7cb05e8463f7f8463b0fd915c.jpg",
      "url_small": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/605775c7cb05e8463f7f8463b0fd915c.small.jpg"
    },
    {
      "id": "890cf5e5b94a255ea4e517d785f53481",
      "similarity": 0.9316171609752804,
      "url": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/890cf5e5b94a255ea4e517d785f53481.jpg",
      "url_small": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/890cf5e5b94a255ea4e517d785f53481.small.jpg"
    }
  ],
  "confirmed": false
}
```

## Check
```https://plant.id/api/check_identifications```

Checks if identifications with given ids have been already proceeded and eventually returns their result.

### Request
When sending the check request, specify your API key and the list of given ids OR your custom ids:

- **`key`**- your [API key](https://web.plant.id/plant-identification-api/)
- **`ids`** - list of ids provided by the identification response
- **`custom_ids`** - list of ids provided by you in the identification request
- `lang` - language code ([ISO 639-1](https://en.m.wikipedia.org/wiki/List_of_ISO_639-1_codes)) used for common names and URLs of plants (default "en")

### Response
You get a list with info about your identifications with given ids. Apart from getting the info you sent with the identification request and the identification result, you can get the following:

- `created` - when was the identification request created
- `sent` - when was the request sent to identification
- `classified` - when was the request classified
<!--- `feedback`-->
- `fail_cause` - cause of the failed identification
- `countable` - whether the identification meets the required properties to be countable according to SLA

## Confirm
```https://api.plant.id/confirm/SUGGESTION_ID```

Confirm suggestion with `SUGGESTION_ID` and unconfirm all others. Use when your plant matches our identification.

### Request
There is one required parameter:
- **`key`**- your [API key](https://web.plant.id/plant-identification-api/)

## Unconfirm
```https://api.plant.id/unconfirm/SUGGESTION_ID```

Unconfirm previously confirmed suggestion with `SUGGESTION_ID`.

### Request
There is one required parameter:
- **`key`**- your [API key](https://web.plant.id/plant-identification-api/)

## Usage info
```https://api.plant.id/usage_info```
Get stats about your API key limits and usage.

### Request
There is one required parameter:
- **`key`**- your [API key](https://web.plant.id/plant-identification-api/)

### Response
Example output:
```
{
  "active": True,
  "daily_limit": None,
  "weekly_limit": 200,
  "monthly_limit": None,
  "total_limit": None,
  "is_closed": False,
  "used_day": 5,
  "used_week": 5,
  "used_month": 11,
  "used_total": 11,
  "remaining_day": None,
  "remaining_week": 195,
  "remaining_month": None,
  "remaining_total": None
}
```

## Plant info
```https://api.plant.id/plant_info```
Get the list of plants known by model.

### Request
There is one required parameter:
- **`key`**- your [API key](https://web.plant.id/plant-identification-api/)

### Response
- `name` - plant names which are known by the model
- `name_genus` - genera which are known by the model
- _(`plant parts` - currently not used)_

Output example:
```
{
  "name": {
    "classes": ["Abelia", "Abelia grandiflora", ...],
    "size": 10997
  },
  "name_genus": {
    "classes": ["Abelia", "Abelmoschus", ...],
    "size": 3173
  },
  "plant_part": {
    "classes": ["bark", "flower", "fruit", "habit", "leaf"],
    "size": 5
  }
}
```

# Examples
Simple code which shows how to work with Plant.id API.

- [Python example](https://github.com/Plant-id/plant-id-examples/blob/master/python/plant_id_client.py)
- [Android/java example](https://github.com/Plant-id/plant-id-examples/tree/master/android)
