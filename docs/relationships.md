# Relationship Endpoints

Action | Path | Description
--- | --- | ---
GET | [/users/self/follows](#GET-/users/self/follows) | Get the list of users this user follows.
GET | [/users/self/followed-by](#GET-/users/self/followed-by) | Get the list of users this user is followed by.
GET | [/users/self/requested-by](#GET-/users/self/requested-by) | List the users who have requested to follow.
GET | [/users/user-id/relationship](#GET-/users/user-id/relationship) | Get information about a relationship to another user.
POST | [/users/user-id/relationship](#POST-/users/user-id/relationship) | Modify the relationship with target user.

## GET /users/self/follows

https://api.instagram.com/v1/users/self/follows?access_token=ACCESS-TOKEN

Get the list of users this user follows.

### REQUIREMENTS

+ **Scope** follower_list

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE
```json
{
    "data": [{
        "username": "kevin",
        "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
        "full_name": "Kevin Systrom",
        "id": "3"
    },
    {
        "username": "instagram",
        "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
        "full_name": "Instagram",
        "id": "25025320"
    }]
}
```

## GET /users/self/followed-by

https://api.instagram.com/v1/users/self/followed-by?access_token=ACCESS-TOKEN

Get the list of users this user is followed by.

### REQUIREMENTS

+ **Scope** follower_list

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE
```json
{
    "data": [{
        "username": "kevin",
        "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
        "full_name": "Kevin Systrom",
        "id": "3"
    },
    {
        "username": "instagram",
        "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
        "full_name": "Instagram",
        "id": "25025320"
    }]
}
```

## GET /users/self/requested-by

https://api.instagram.com/v1/users/self/requested-by?access_token=ACCESS-TOKEN

List the users who have requested this user's permission to follow.

### REQUIREMENTS

+ **Scope** follower_list

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE
```json
{
    "data": [
        {
            "username": "mikeyk",
            "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_4_75sq_1292324747_debug.jpg",
            "id": "4"
        }
    ]
}
```

## GET /users/user-id/relationship

https://api.instagram.com/v1/users/{user-id}/relationship?access_token=ACCESS-TOKEN

Get information about a relationship to another user. Relationships are expressed using the following terms in the response:

outgoing_status: Your relationship to the user. Can be 'follows', 'requested', 'none'.
incoming_status: A user's relationship to you. Can be 'followed_by', 'requested_by', 'blocked_by_you', 'none'.

### REQUIREMENTS

+ **Scope** follower_list

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.

### RESPONSE
```json
{
    "data": {
        "outgoing_status": "none",
        "incoming_status": "requested_by"
    }
}
```

## POST /users/user-id/relationship

https://api.instagram.com/v1/users/{user-id}/relationship?access_token=ACCESS-TOKEN

Modify the relationship between the current user and the target user. You need to include an action parameter to specify the relationship action you want to perform. Valid actions are: 'follow', 'unfollow' 'approve' or 'ignore'. Relationships are expressed using the following terms in the response:

+ **outgoing_status**: Your relationship to the user. Can be 'follows', 'requested', 'none'.
+ **incoming_status**: A user's relationship to you. Can be 'followed_by', 'requested_by', 'blocked_by_you', 'none'.

### REQUIREMENTS

+ **Scope** relationships

### PARAMETERS

+ **ACCESS_TOKEN** A valid access token.
+ **ACTION** follow | unfollow | approve | ignore

### RESPONSE
```json
{
    "data": {
        "outgoing_status": "requested"
    }
}
```