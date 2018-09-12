# Location Endpoints

Action | Path | Description
--- | --- | ---
GET | [/locations/location-id](#GET-/locations/location-id) | Get information about a location.
GET | [/locations/location-id/media/recent](#GET-/locations/location-id/media/recent) | Get a list of media objects from a given location.
GET | [/locations/search](#GET-/locations/search) | Search for a location by geographic coordinate.

## GET /locations/location-id

https://api.instagram.com/v1/locations/{location-id}?access_token=ACCESS-TOKEN

Get information about a location.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
    "data": {
        "id": "1",
        "name": "Dogpatch Labs",
        "latitude": 37.782,
        "longitude": -122.387,
    }
}
```

## GET /locations/location-id/media/recent

https://api.instagram.com/v1/locations/{location-id}/media/recent?access_token=ACCESS-TOKEN

Get a list of recent media objects from a given location.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **MAX_ID** Return media after this max_id.
+ **MIN_ID** Return media before this min_id.
  
### RESPONSE

```json
{
    "data": [{
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": ["expobar"],
        "comments": {
            "count": 0
        },
        "caption": {
            "created_time": "1296532028",
            "text": "@mikeyk pulls a shot on our #Expobar",
            "from": {
                "username": "josh",
                "full_name": "Josh Riedel",
                "type": "user",
                "id": "33"
            },
            "id": "25663923"
        },
        "likes": {
            "count": 35
        },
        "link": "http://instagr.am/p/BUS3X/",
        "user": {
            "username": "josh",
            "profile_picture": "...",
            "id": "33"
        },
        "created_time": "1296531955",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/01/31/32d364527512437a8a17ba308a7c83bb_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/01/31/32d364527512437a8a17ba308a7c83bb_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/01/31/32d364527512437a8a17ba308a7c83bb_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "user_has_liked": false,
        "id": "22097367",
        "location": {
            "latitude": 37.780885099999999,
            "id": "514276",
            "longitude": -122.3948632,
            "name": "Instagram"
        }
    },
    {
        "type": "video",
        "videos": {
            "low_resolution": {
                "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
                "width": 480,
                "height": 480
            },
            "standard_resolution": {
                "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
                "width": 640,
                "height": 640
            },
        "users_in_photo": null,
        "filter": "Vesper",
        "tags": [],
        "comments": {
            "count": 2
        },
        "caption": null,
        "likes": {
            "count": 1
        },
        "link": "http://instagr.am/p/D/",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "...",
            "id": "3"
        },
        "created_time": "1279340983",
        "images": {
            "low_resolution": {
                "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "id": "3",
        "location": {
            "latitude": 37.780885099999999,
            "id": "514276",
            "longitude": -122.3948632,
            "name": "Instagram"
        }
    },
    ...]
}
```

## GET /locations/search

https://api.instagram.com/v1/locations/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN

Search for a location by geographic coordinate.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **LAT** Latitude of the center search coordinate. If used, lng is required.
+ **LNG** Longitude of the center search coordinate. If used, lat is required.
+ **DISTANCE** Default is 500m (distance=500), max distance is 750.
+ **FACEBOOK_PLACES_ID** Returns a location mapped off of a Facebook places id. If used, lat and lng are not required.

### RESPONSE

```json
{
    "data": [{
        "id": "788029",
        "latitude": 48.858844300000001,
        "longitude": 2.2943506,
        "name": "Eiffel Tower, Paris"
    },
    {
        "id": "545331",
        "latitude": 48.858334059662262,
        "longitude": 2.2943401336669909,
        "name": "Restaurant 58 Tour Eiffel"
    },
    {
        "id": "421930",
        "latitude": 48.858325999999998,
        "longitude": 2.294505,
        "name": "American Library in Paris"
    }]
}
```
