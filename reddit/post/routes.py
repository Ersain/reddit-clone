from reddit import reddit
from reddit.reddit_api import subreddit_request
from reddit.utility import get_submission_comments
from flask import render_template, Blueprint


post_bp = Blueprint('post', __name__)


@post_bp.route("/")
@post_bp.route('/home')
def home():
    posts = reddit.front.hot(limit=15)
    return render_template("home.html", posts=posts)


@post_bp.route("/r/<string:subreddit>")
def subreddit_route_api(subreddit):
    posts = subreddit_request(subreddit)
    return render_template("home_api.html", posts=posts['data']['children'])


@post_bp.route('/post/<string:post_id>')
def post(post_id):
    post = reddit.submission(id=post_id)
    comments = get_submission_comments(post, 10)
    return render_template('post.html', post=post, comments=comments)
