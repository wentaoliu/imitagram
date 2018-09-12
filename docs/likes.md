# Like Endpoints

Action | Path | Description
--- | --- | ---
GET | [/media/media-id/likes](#GET-/media/media-id/likes) | Get a list of users who have liked this media.
POST | [/media/media-id/likes](#POST-/media/media-id/likes) | Set a like on this media by the current user.
DEL | [/media/media-id/likes](#DEL-/media/media-id/likes) | Remove a like on this media by the current user.

## GET /media/media-id/likes

https://api.instagram.com/v1/media/{media-id}/likes?access_token=ACCESS-TOKEN

Get a list of users who have liked this media.

The public_content scope is required for media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** public_content

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE

```json
{
    "data": [{
        "username": "jack",
        "first_name": "Jack",
        "last_name": "Dorsey",
        "type": "user",
        "id": "66"
    },
    {
        "username": "sammyjack",
        "first_name": "Sammy",
        "last_name": "Jack",
        "type": "user",
        "id": "29648"
    }]
}
```

## POST /media/media-id/likes

curl -F 'access_token=ACCESS-TOKEN' \
    https://api.instagram.com/v1/media/{media-id}/likes

Set a like on this media by the currently authenticated user.

The public_content scope is required for media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** likes, public_content

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

## DEL /media/media-id/likes

curl -X DELETE https://api.instagram.com/v1/media/{media-id}/likes?access_token=ACCESS-TOKEN

Remove a like on this media by the currently authenticated user.

The public_content scope is required for media that does not belong to the owner of the access_token.

### REQUIREMENTS

+ **Scope** likes, public_content

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
