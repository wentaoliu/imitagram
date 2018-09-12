# Tag Endpoints

Action | Path | Description
--- | --- | ---
GET | [/tags/tag-name](#GET-/tags/tag-name) | Get information about a tag object.
GET | [/tags/tag-name/media/recent](#GET-/tags/tag-name/media/recent) | Get a list of recently tagged media.
GET | [/tags/search](#GET-/tags/search) | Search for tags by name.

## GET /tags/tag-name

https://api.instagram.com/v1/tags/{tag-name}?access_token=ACCESS-TOKEN

Get information about a tag object.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ 
### RESPONSE

```json
{
    "data": {
        "media_count": 472,
        "name": "nofilter",
    }
}
```

## GET /tags/tag-name/media/recent

https://api.instagram.com/v1/tags/{tag-name}/media/recent?access_token=ACCESS-TOKEN

Get a list of recently tagged media.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **MAX_TAG_ID** Return media after this max_tag_id.
+ **MIN_TAG_ID** Return media before this min_tag_id.
+ **COUNT** Count of tagged media to return.

### RESPONSE

```json
{
    "data": [{
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": ["snow"],
        "comments": {
            "count": 3
        },
        "caption": {
            "created_time": "1296703540",
            "text": "#Snow",
            "from": {
                "username": "emohatch",
                "id": "1242695"
            },
            "id": "26589964"
        },
        "likes": {
            "count": 1
        },
        "link": "http://instagr.am/p/BWl6P/",
        "user": {
            "username": "emohatch",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1242695_75sq_1293915800.jpg",
            "id": "1242695",
            "full_name": "Dave"
        },
        "created_time": "1296703536",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/f9443f3443484c40b4792fa7c76214d5_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/f9443f3443484c40b4792fa7c76214d5_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/f9443f3443484c40b4792fa7c76214d5_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "id": "22699663",
        "location": null
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
        "tags": ["snow"],
        "comments": {
            "count": 2
        },
        "caption": {
            "created_time": "1296703540",
            "text": "#Snow",
            "from": {
                "username": "emohatch",
                "id": "1242695"
            },
            "id": "26589964"
        },
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
        "location": null
    },
    ...]
}
```

## GET /tags/search

https://api.instagram.com/v1/tags/search?q=snowy&access_token=ACCESS-TOKEN

Search for tags by name.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **Q** A valid tag name without a leading #. (eg. snowy, nofilter)

### RESPONSE

```json
{
    "data": [
        {
            "media_count": 43590,
            "name": "snowy"
        },
        {
            "media_count": 3264,
            "name": "snowyday"
        },
        {
            "media_count": 1880,
            "name": "snowymountains"
        }
    ]
}
```
