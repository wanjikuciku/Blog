from flask import render_template
from app import app
from .request import get_blog

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting popular blog
    popular_blog = get_blog('popular')
    upcoming_blog = get_blog('upcoming')
    now_showing_blog = get_blog('now_playing')
    print(popular_blog)
    title = 'Home - Welcome to The best blog site'
    return render_template('index.html', title = title,popular = popular_blog,upcoming = upcoming_blog, now_showing = now_showing_blog)