from reddit import reddit
from reddit.utility import format_img_link, get_redditor_comments
from flask import render_template, Blueprint

user_bp = Blueprint('user', __name__)


@user_bp.route("/u/<username>")
def user(username):
    user = reddit.redditor(username)
    comments = get_redditor_comments(user, 10)
    avatar_link = format_img_link(user.icon_img)
    return render_template('user.html', user=user, avatar=avatar_link, comments=comments)
