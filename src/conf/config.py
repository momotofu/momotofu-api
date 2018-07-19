import os

class DevelopmentConfig(object):
    DEBUG = False
    TESTING = False

    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])
    SECRET_KEY = 'super_secret_key'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    CREDENTIALS_PATH = os.path.abspath('credentials/config.json')
    DEBUG = True
