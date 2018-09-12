# Media Endpoints

Action | Path | Description
--- | --- | ---
GET | [/media/media-id](#GET-/media/media-id) | Get information about a media object.
GET | [/media/shortcode/shortcode](#GET-/media/shortcode/shortcode) | Get information about a media object.
GET | [/media/search](#GET-/media/search) | Search for recent media in a given area.

## GET /media/media-id

https://api.instagram.com/v1/media/{media-id}?access_token=ACCESS-TOKEN

Get information about a media object. Use the type field to differentiate between image and video media in the response. You will also receive the user_has_liked field which tells you whether the owner of the access_token has liked this media.

The public_content permission scope is required to get a media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
    "data": {
        "type": "image",
        "users_in_photo": [{
            "user": {
                "username": "kevin",
                "full_name": "Kevin S",
                "id": "3",
                "profile_picture": "..."
            },
            "position": {
                "x": 0.315,
                "y": 0.9111
            }
        }],
        "filter": "Walden",
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
                "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "id": "3",
        "location": null
    }
}

/*------------
Video Example
-------------*/

{
    "data": {
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
        "location": null
    }
}

/*------------
Carousel Example
-------------*/

{
  "data": {
      "type": "image",
      "users_in_photo": [{
          "user": {
              "username": "kevin",
              "full_name": "Kevin S",
              "id": "3",
              "profile_picture": "..."
          },
          "position": {
              "x": 0.315,
              "y": 0.9111
          }
      }],
      "filter": "Walden",
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
              "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41ca_6.jpg",
              "width": 306,
              "height": 306
          },
          "thumbnail": {
              "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41ca_5.jpg",
              "width": 150,
              "height": 150
          },
          "standard_resolution": {
              "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_7.jpg",
              "width": 612,
              "height": 612
          }
      },
      "carousel_media": [
          {
              "images": {
                  "thumbnail": {
                      "width": 150,
                      "height": 150,
                      "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372_6.jpg"
                  },
                  "low_resolution": {
                      "width": 320,
                      "height": 320,
                      "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372_5.jpg"
                  },
                  "standard_resolution": {
                      "width": 640,
                      "height": 640,
                      "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372_7.jpg"
                  }
              },
              "users_in_photo": [{
                  "user": {
                      "id": "4758430517",
                      "full_name": "radkul",
                      "profile_picture": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372_6.jpg",
                      "username": "igradkul"},
                      "position": {
                          "x": 0.6773333333333333,
                          "y": 0.36
                      }
                  }
              ],
              "type": "image"
          },
          {
              "videos": {
                  "standard_resolution": {
                      "width": 640,
                      "height": 640,
                      "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4"
                  },
                  "low_bandwidth": {
                      "width": 480,
                      "height": 480,
                      "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4"
                  },
                  "low_resolution": {
                      "width": 480,
                      "height": 480,
                      "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_103.mp4"
                    }
                },
                "users_in_photo": [],
                "type": "video"
            }
      ],
      "id": "3",
      "location": null
  }
}
```

## GET /media/shortcode/shortcode

https://api.instagram.com/v1/media/shortcode/D?access_token=ACCESS-TOKEN

This endpoint returns the same response as GET /media/media-id.
A media object's shortcode can be found in its shortlink URL. An example shortlink is http://instagram.com/p/tsxp1hhQTG/. Its corresponding shortcode is tsxp1hhQTG.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
    "data": {
        "type": "image",
        "users_in_photo": [{
            "user": {
                "username": "kevin",
                "full_name": "Kevin S",
                "id": "3",
                "profile_picture": "..."
            },
            "position": {
                "x": 0.315,
                "y": 0.9111
            }
        }],
        "filter": "Walden",
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
                "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "id": "3",
        "location": null
    }
}

/*------------
Video Example
-------------*/

{
    "data": {
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
        "location": null
    }
}
```

## GET /media/search

https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN

Search for recent media in a given area.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **LAT** Latitude of the center search coordinate. If used, lng is required.
+ **LNG** Longitude of the center search coordinate. If used, lat is required.
+ **DISTANCE** Default is 1km (distance=1000), max distance is 5km.

### RESPONSE

```json
{
    "data": [{
        "distance": 41.741369194629698,
        "type": "image",
        "users_in_photo": [],
        "filter": "Earlybird",
        "tags": [],
        "comments": {
            "count": 2
        },
        "caption": null,
        "likes": {
            "count": 1
        },
        "link": "http://instagr.am/p/BQEEq/",
        "user": {
            "username": "mahaface",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1329896_75sq_1294131373.jpg",
            "id": "1329896"
        },
        "created_time": "1296251679",
        "images": {
            "low_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/01/28/0cc4f24f25654b1c8d655835c58b850a_6.jpg",
                "width": 306,
                "height": 306
            },
            "thumbnail": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/01/28/0cc4f24f25654b1c8d655835c58b850a_5.jpg",
                "width": 150,
                "height": 150
            },
            "standard_resolution": {
                "url": "http://distillery.s3.amazonaws.com/media/2011/01/28/0cc4f24f25654b1c8d655835c58b850a_7.jpg",
                "width": 612,
                "height": 612
            }
        },
        "id": "20988202",
        "location": null
    },
    {
        "distance": 41.741369194629698,
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
        "location": null
    }
}
```
