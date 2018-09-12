# User Endpoints

Action | Path | Description
--- | --- | ---
GET | [/users/self](#GET-/users/self) | Get information about the owner of the access token.
GET | [/users/user-id](#GET-/users/user-id) | Get information about a user.
GET | [/users/self/feed](#GET-/users/self/feed) | See the authenticated user's feed.
GET | [/users/self/media/recent](#GET-/users/self/media/recent) | Get the most recent media of the user.
GET | [/users/user-id/media/recent](#GET-/users/user-id/media/recent) | Get the most recent media of a user.
GET | [/users/self/media/liked](#GET-/users/self/media/liked) | Get the recent media liked by the user.
GET | [/users/search](#GET-/users/search) | Search for a user by name.

## GET /users/self

https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN

Get information about the owner of the access_token.

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
  "data": {
    "id": "1574083",
    "username": "snoopdogg",
    "full_name": "Snoop Dogg",
    "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
    "bio": "This is my bio",
    "website": "http://snoopdogg.com",
    "is_business": false,
    "counts": {
      "media": 1320,
      "follows": 420,
      "followed_by": 3410
    }
  }
}
```

## GET /users/user-id

https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN

Get information about a user.

The public_content scope is required if the user is not the owner of the access_token.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN**	A valid access token.

### RESPONSE

```json
{
    "data": {
        "id": "1574083",
        "username": "snoopdogg",
        "full_name": "Snoop Dogg",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
        "bio": "This is my bio",
        "website": "http://snoopdogg.com",
        "counts": {
            "media": 1320,
            "follows": 420,
            "followed_by": 3410
        }
}
```

## GET /users/self/feed

https://api.instagram.com/v1/users/self/feed?access_token=ACCESS-TOKEN

See the authenticated user's feed.

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **COUNT** Count of media to return.
+ **MIN_ID** Return media later than this min_id.
+ **MAX_ID** Return media earlier than this max_id.s

### RESPONSE

```json
{
    "data": [{
        "location": {
            "id": "833",
            "latitude": 37.77956816727314,
            "longitude": -122.41387367248539,
            "name": "Civic Center BART"
        },
        "comments": {
            "count": 16,
            "data": [ ... ]
        },
        "caption": null,
        "link": "http://instagr.am/p/BXsFz/",
        "likes": {
            "count": 190,
            "data": [{
                "username": "shayne",
                "full_name": "Shayne Sweeney",
                "id": "20",
                "profile_picture": "..."
            }, {...subset of likers...}]
        },
        "created_time": "1296748524",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": [],
        "id": "22987123",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        }
    },
    {
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
        "comments": {
            "data": [{
                "created_time": "1279332030",
                "text": "Love the sign here",
                "from": {
                    "username": "mikeyk",
                    "full_name": "Mikey Krieger",
                    "id": "4",
                    "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1242695_75sq_1293915800.jpg"
                },
                "id": "8"
            },
            {
                "created_time": "1279341004",
                "text": "Chilako taco",
                "from": {
                    "username": "kevin",
                    "full_name": "Kevin S",
                    "id": "3",
                    "profile_picture": "..."
                },
                "id": "3"
            }],
            "count": 2
        },
        "caption": null,
        "likes": {
            "count": 1,
            "data": [{
                "username": "mikeyk",
                "full_name": "Mikeyk",
                "id": "4",
                "profile_picture": "..."
            }]
        },
        "link": "http://instagr.am/p/D/",
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
        "type": "video",
        "users_in_photo": null,
        "filter": "Vesper",
        "tags": [],
        "id": "363839373298",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        },
        "location": null
    },
    ...]
}
```

## GET /users/self/media/recent

https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN

Get the most recent media published by the owner of the access_token.

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **MAX_ID** Return media earlier than this max_id.
+ **MIN_ID** Return media later than this min_id.
+ **COUNT** Count of media to return.

### RESPONSE

```json
{
    "data": [{
        "comments": {
            "count": 0
        },
        "caption": {
            "created_time": "1296710352",
            "text": "Inside le truc #foodtruck",
            "from": {
                "username": "kevin",
                "full_name": "Kevin Systrom",
                "type": "user",
                "id": "3"
            },
            "id": "26621408"
        },
        "likes": {
            "count": 15
        },
        "link": "http://instagr.am/p/BWrVZ/",
        "user": {
            "username": "kevin",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        },
        "created_time": "1296710327",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": ["foodtruck"],
        "id": "22721881",
        "location": {
            "latitude": 37.778720183610183,
            "longitude": -122.3962783813477,
            "id": "520640",
            "street_address": "",
            "name": "Le Truc"
        }
    },
    {
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
        "comments": {
            "count": 2
        },
        "caption": null,
        "likes": {
            "count": 1
        },
        "link": "http://instagr.am/p/D/",
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
        "type": "video",
        "users_in_photo": null,
        "filter": "Vesper",
        "tags": [],
        "id": "363839373298",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        },
        "location": null
    },
   ]
}
```

## GET /users/user-id/media/recent

https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN

Get the most recent media published by a user.

The public_content scope is required if the user is not the owner of the access_token.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **MAX_ID** Return media earlier than this max_id.
+ **MIN_ID** Return media later than this min_id.
+ **COUNT** Count of media to return.

### RESPONSE

```json
{
    "data": [{
        "comments": {
            "count": 0
        },
        "caption": {
            "created_time": "1296710352",
            "text": "Inside le truc #foodtruck",
            "from": {
                "username": "kevin",
                "full_name": "Kevin Systrom",
                "type": "user",
                "id": "3"
            },
            "id": "26621408"
        },
        "likes": {
            "count": 15
        },
        "link": "http://instagr.am/p/BWrVZ/",
        "user": {
            "username": "kevin",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        },
        "created_time": "1296710327",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": ["foodtruck"],
        "id": "22721881",
        "location": {
            "latitude": 37.778720183610183,
            "longitude": -122.3962783813477,
            "id": "520640",
            "street_address": "",
            "name": "Le Truc"
        }
    },
    {
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
        "comments": {
            "count": 2
        },
        "caption": null,
        "likes": {
            "count": 1
        },
        "link": "http://instagr.am/p/D/",
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
        "type": "video",
        "users_in_photo": null,
        "filter": "Vesper",
        "tags": [],
        "id": "363839373298",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        },
        "location": null
    },
   ]
}
```

## GET /users/self/media/liked

https://api.instagram.com/v1/users/self/media/liked?access_token=ACCESS-TOKEN

Get the list of recent media liked by the owner of the access_token.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **MAX_LIKE_ID** Return media liked before this id.
+ **COUNT** Count of media to return.

### RESPONSE

```json
{
    "data": [{
        "location": {
            "id": "833",
            "latitude": 37.77956816727314,
            "longitude": -122.41387367248539,
            "name": "Civic Center BART"
        },
        "comments": {
            "count": 16
        },
        "caption": null,
        "link": "http://instagr.am/p/BXsFz/",
        "likes": {
            "count": 190
        },
        "created_time": "1296748524",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": [],
        "id": "22987123",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        }
    },
    {
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
        "comments": {
            "count": 2
        },
        "caption": null,
        "likes": {
            "count": 1
        },
        "link": "http://instagr.am/p/D/",
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
        "type": "video",
        "users_in_photo": null,
        "filter": "Vesper",
        "tags": [],
        "id": "363839373298",
        "user": {
            "username": "kevin",
            "full_name": "Kevin S",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
            "id": "3"
        },
        "location": null
    },
    ...]
}
```

## GET /users/search

https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN

Get a list of users matching the query.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **Q** A query string.
+ **COUNT** Number of users to return.

### RESPONSE

```json
{
    "data": [{
        "username": "jack",
        "first_name": "Jack",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_66_75sq.jpg",
        "id": "66",
        "last_name": "Dorsey"
    },
    {
        "username": "sammyjack",
        "first_name": "Sammy",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_29648_75sq_1294520029.jpg",
        "id": "29648",
        "last_name": "Jack"
    },
    {
        "username": "jacktiddy",
        "first_name": "Jack",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_13096_75sq_1286441317.jpg",
        "id": "13096",
        "last_name": "Tiddy"
    }]
}
```
