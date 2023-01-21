from app import app


def test_get_posts_api():
    response = app.test_client().get("/api/posts")
    assert type(response.json) == list
    print(response.json[0].keys)
    assert set(response.json[0].keys()) == {
               "poster_name",
               "poster_avatar",
               "pic", "content",
               "views_count",
               "likes_count",
               "pk"
           }


def test_get_post_api():

    response = app.test_client().get("/api/posts/1")
    assert type(response.json) == dict

    assert set(response.json.keys()) == {
               "poster_name",
               "poster_avatar",
               "pic", "content",
               "views_count",
               "likes_count",
               "pk"
           }

