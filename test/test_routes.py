from flask import Flask
from reddit import app
from reddit.post import routes as post_routes


def test_home_route():
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_subreddit_route():
    client = app.test_client()
    url = '/r/python'

    response = client.get(url)
    assert response.status_code == 200


def test_user_route():
    client = app.test_client()
    url = '/user/mag1skboy'

    response = client.get(url)
    assert response.status_code == 200


def test_post_route():
    client = app.test_client()
    url = '/post/c0i68l'

    response = client.get(url)
    assert response.status_code == 200