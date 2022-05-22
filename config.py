import os

from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.environ['APP_HOST']
APP_PORT = int(os.environ['APP_PORT'])
SSL_CERTFILE = os.environ.get('SSL_CERTFILE')
SSL_KEYFILE = os.environ.get('SSL_KEYFILE')
