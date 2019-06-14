import requests
import json
from datetime import datetime

link = 'https://www.reddit.com'


def subreddit_request(subreddit):
    r = requests.get(link+'/r/'+subreddit+'.json',
                     headers={'User-agent': 'your bot 0.1'})
    return r.json()


def user_request(username):
    r = requests.get(link+'/u/'+username+'/about.json',
                     headers={'User-agent': 'your bot 0.1'})
    return r.json()


def user_history(username):
    r = requests.get(link+'/u/'+username+'.json',
                     headers={'User-agent': 'your bot 0.1'})
    return r.json()


def convert_time(time):
    ts = int(time)
    return (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d'))
