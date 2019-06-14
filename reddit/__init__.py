from flask import Flask
import praw

app = Flask(__name__)
app.config['SECRET_KEY'] = '23b005f15663039761bc'

reddit = praw.Reddit(client_id='29kEC9wIc7F3ww', \
                     client_secret='vdRcAJ_ZuuO3YyceKpMBOKV88EI', \
                     user_agent='Reddit Api usage', \
                     username='mag1skboy')

# from redditApp import routes

from reddit.user.routes import user_bp
from reddit.post.routes import post_bp
from reddit.search.routes import search_bp

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(search_bp)
