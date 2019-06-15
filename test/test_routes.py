import sys
sys.path.append("..")

from flask import Flask
from reddit import app
from reddit.post import routes as post_routes
from reddit.user import routes as user_routes


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


def test_search_route_1():
    client = app.test_client()
    url = '/search/subreddit'
    
    response = client.get(url)
    assert response.status_code == 200


def test_search_route_2():
    client = app.test_client()
    url = '/search/user'
    
    response = client.get(url)
    assert response.status_code == 200


test_home_route()
test_subreddit_route()
test_user_route()
test_post_route()
test_search_route_1()
test_search_route_2()