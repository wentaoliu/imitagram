# Imitagram

## Tables

User
    email
    username
    password_en
    full_name
    profile_photo
    following_count
    follower_count
    posts_count

relationship
    source
    sink
    datetime

media
    (id)
    user_id
    type
    comments_count
    likes_count
    created_time
    location
    images_thumbnail
    images_standard

comments
    media_id
    id
    created_time
    user_id
    text

likes
    media_id
    user_id
    created_time

activity
    actor
    verb
    object
    target
    created_time