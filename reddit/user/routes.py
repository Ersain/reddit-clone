from reddit.reddit_api import user_history, user_request, convert_time
from reddit import reddit
from reddit.utility import format_img_link, get_redditor_comments
from flask import render_template, Blueprint

user_bp = Blueprint('user', __name__)


@user_bp.route("/user/<string:username>")
def user_api(username):
    user = user_request(username)
    user_his = user_history(username)
    time = convert_time(user['data']['created_utc'])
    return render_template('user_api.html', user=user['data'], history=user_his['data']['children'], time=time)
