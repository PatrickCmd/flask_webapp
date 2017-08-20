# default configurations
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xde\x0e@Q\xd4\xc9\xf8n\x14\x91)\xfa\xd6\x14\xf5\xe8It\xfa\x08\xb7\xf0\x1f\xe9'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # DATABASE_URL = 'postgresql://postgres:arsenal2016@localhost/flask_webapp'


# Testing Config
class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Development config
class DevelopmentConfig(BaseConfig):
    DEBUG = True


# Production config
class ProductionConfig(BaseConfig):
    DEBUG = False