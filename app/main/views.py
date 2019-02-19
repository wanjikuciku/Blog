from flask import render_template,redirect,url_for,abort, request
from . import main
from ..models import User,Blog
from .forms import BlogForm,AddAuthor
from .. import db
from flask.views import View, MethodView
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
        title = form.title.data
        description = form.description.data
        
        new_blog = Blog(blog=blog)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form=form)
@main.route('/all_blogs')
def blog():
    blogs = Blog.query.order_by(Blog.date_posted.desc())
    return render_template('blogs.html', blogs=blogs)


@main.route('/blogs/<int:blog_id>',methods = ["GET","POST"])
def view_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return redirect(url_for('main.view_blog', blog_id=blog.id))
    return render_template("blogs.html", blog_form=form, blog=blog, random = random)