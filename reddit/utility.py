import datetime, time, sys
from reddit import praw, reddit
from prawcore import NotFound
from praw.models import Redditor
from werkzeug.routing import BuildError

def get_submission_comments(submission, n):
    comments = []
    i = 1
    for comment in submission.comments:
        if i >= n:
            break
        if isinstance(comment, praw.models.MoreComments):
            continue
        comments.append(comment)
        i += 1
    return comments


def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def redditor_exists(name):
    try:
        user = reddit.redditor(name)
        user.created_utc
    except (NotFound, TypeError, BuildError):
        return False
    return True
