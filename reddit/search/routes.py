from reddit.utility import sub_exists, redditor_exists
from reddit import reddit
from reddit.search.forms import SearchForSubredditForm, SearchForUserForm
from flask import flash, request, redirect, render_template, url_for, Blueprint

search_bp = Blueprint('search', __name__)


@search_bp.route("/search/subreddit", methods=['GET', 'POST'])
def search_for_subreddit():
    form = SearchForSubredditForm()
    if form.validate_on_submit():
        if sub_exists(form.search.data):
            return redirect(url_for('post.subreddit_route_api', subreddit=form.search.data))
        else:
            flash("A subreddit with the name " + "'" +
                  form.search.data + "'" + " does not exist.", 'danger')
    return render_template('search.html', form=form)


@search_bp.route("/search/user", methods=['GET', 'POST'])
def search_for_user():
    form = SearchForUserForm()
    if form.validate_on_submit():
        if redditor_exists(form.search.data):
            return redirect(url_for('user.user_api', username=form.search.data))
        else:
            flash("A redditor with the name " + "'" +
                  form.search.data + "'" + " does not exist.", 'danger')
    return render_template('search.html', form=form)
