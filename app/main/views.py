from flask import render_template,redirect,url_for,abort, request
from . import main
from .forms import BlogForm,AddAuthor
from flask_login import login_required
import requests
import json


@main.route('/')
def index():
    
    blog = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return render_template('index.html', blog = blog )

@main.route('/blog/new/', methods=['GET', 'POST'])
@login_required
def new_blog():
    '''
    Function that creates new bloges
    '''
    form = BlogForm()

    if form.validate_on_submit():
        blog = form.content.data
        category = form.category.data
        new_blog = blog(blog=blog, category=category)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form=form)

