import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    USER = os.environ.get('DB_USER')
    PASSWORD = os.environ.get('DB_PASSWORD')
    HOST = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')
    DB = os.environ.get('DB_NAME')
    TG_TOKEN = os.environ.get('TG_TOKEN')

    ASKIID_CLIENT_ID = os.environ.get('ASKIID_CLIENT_ID')
    ASKIID_CLIENT_SECRET = os.environ.get('ASKIID_CLIENT_SECRET')
    ASKIID_CALLBACK_URL = os.environ.get('ASKIID_CALLBACK_URL')


    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data\\data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'casdjhfvcsduyfvchsdevfsedvfhnsdhnv384734r3hqrh34trw34etfh347tu34hyjg483utghgug'
