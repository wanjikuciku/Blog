import os

class Config:
    '''
    General configuration parent class
    '''
    BLOG_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}