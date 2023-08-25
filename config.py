import os

class Config(object):
    """
    Base config class
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A hard to guess string'
    LOG_FILE = 'logs/app.log' # Example log file path

    # Database configurations, if you're using a database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Any other configurations that your app globally needs

class DevelopmentConfig(Config):
    """
    Development config for the project
    """
    DEBUG = True
    # Development specific configs e.g.
    # DATABASE_URI = 'your_dev_db_uri'

class TestingConfig(Config):
    """
    Testing config for the project
    """
    TESTING = True
    # Testing specific configs e.g.
    # DATABASE_URI = 'your_test_db_uri'

class ProductionConfig(Config):
    """
    Production config for the project
    """
    # Production specific configs e.g.
    # DATABASE_URI = 'your_prod_db_uri'
