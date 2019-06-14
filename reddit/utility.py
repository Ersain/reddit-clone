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

def is_valid_comment(comment):
    if isinstance(comment, praw.models.MoreComments):
        return False
    if isinstance(comment, praw.models.comment_forest.CommentForest):
        return False
    return True

def get_redditor_comments(redditor, n):
    comments = []
    i = 1
    for comment in redditor.comments.new():
        if i >= n:
            break
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

def format_img_link(link):
    if '?' in link:
        return link.split('?')[0]
    return link