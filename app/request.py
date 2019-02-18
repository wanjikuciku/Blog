from app import app
import urllib.request,json
from .models import blog

Blog = blog.Blog

# Getting the blog base url
base_url = app.config["BLOG_API_BASE_URL"]

def get_blog(category):
    '''
    Function that gets the json response to our url request
    '''
    get_blog_url = base_url.format(category)

    with urllib.request.urlopen(get_blog_url) as url:
        get_blog_data = url.read()
        get_blog_response = json.loads(get_blog_data)

        blog_results = None

        if get_blog_response['results']:
            blog_results_list = get_blog_response['results']
            blog_results = process_results(blog_results_list)


    return blog_results

def process_results(blog_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        blog_list: A list of dictionaries that contain movie details

    Returns :
        blog_results: A list of blog objects
    '''
    blog_results = []
    for blog_item in blog_list:
        id = blog_item.get('id')
        title = blog_item.get('original_title')
        overview = blog_item.get('overview')
        poster = blog_item.get('poster_path')
        vote_average = blog_item.get('vote_average')
        vote_count = blog_item.get('vote_count')

        if poster:
            blog_object = Blog(id,title,overview,poster,vote_average,vote_count)
            blog_results.append(blog_object)

    return blog_results

def get_blog(id):
    get_blog_details_url = base_url.format(id)

    with urllib.request.urlopen(get_blog_details_url) as url:
        blog_details_data = url.read()
        blog_details_response = json.loads(blog_details_data)

        blog_object = None
        if blog_details_response:
            id = blog_details_response.get('id')
            title = blog_details_response.get('original_title')
            overview = blog_details_response.get('overview')
            poster = blog_details_response.get('poster_path')
            vote_average = blog_details_response.get('vote_average')
            vote_count = blog_details_response.get('vote_count')

            blog_object = Blog(id,title,overview,poster,vote_average,vote_count)

    return blog_object