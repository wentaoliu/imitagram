# Comment Endpoints

Action | Path | Description
--- | --- | ---
GET | [/media/media-id/comments](#GET-/media/media-id/comments) | Get a list of recent comments on a media object.
POST | [/media/media-id/comments](#POST-/media/media-id/comments) | Create a comment on a media object.
DEL | [/media/media-id/comments/comment-id](#DEL-/media/media-id/comments/comment-id) | Remove a comment.

## GET /media/media-id/comments

https://api.instagram.com/v1/media/{media-id}/comments?access_token=ACCESS-TOKEN

Get a list of recent comments on a media object.

The public_content scope is required for media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
    "data": [
        {
            "created_time": "1280780324",
            "text": "Really amazing photo!",
            "from": {
                "username": "snoopdogg",
                "profile_picture": "http://images.instagram.com/profiles/profile_16_75sq_1305612434.jpg",
                "id": "1574083",
                "full_name": "Snoop Dogg"
            },
            "id": "420"
        },
        ...
    ]
}
```

## POST /media/media-id/comments

curl -F 'access_token=ACCESS-TOKEN' \
     -F 'text=This+is+my+comment' \
     https://api.instagram.com/v1/media/{media-id}/comments

Create a comment on a media object with the following rules:

+ The total length of the comment cannot exceed 300 characters.
+ The comment cannot contain more than 4 hashtags.
+ The comment cannot contain more than 1 URL.
+ The comment cannot consist of all capital letters.

The public_content scope is required for media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** comments, public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **TEXT** Text to post as a comment on the media object as specified in media-id.

### RESPONSE

```json
{
    "meta": {
        "code": 200
    }, 
    "data": null
}
```

## DEL /media/media-id/comments/comment-id

curl -X DELETE https://api.instagram.com/v1/media/{media-id}/comments/{comment-id}?access_token=ACCESS-TOKEN

Remove a comment either on the authenticated user's media object or authored by the authenticated user.

The public_content scope is required for media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** comments, public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
    "meta": {
        "code": 200
    }, 
    "data": null
}
```
