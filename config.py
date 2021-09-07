import toml

env = toml.load('env.toml')


class App:
    app = env['App']

    HOST = app['host']
    PORT = app['port']


class Database:
    db = env['Database']

    NAME = db['name']
    HOST = db.get('host')
    PORT = db.get('port')
    USERNAME = db.get('username')
    PASSWORD = db.get('password')
    AUTH_SOURCE = db.get('auth_source', 'admin')


class SSL:
    ssl = env['SSL']

    CERTFILE = ssl.get('certfile')
    KEYFILE = ssl.get('keyfile')


class Secrets:
    secrets = env['Secrets']

    TOKEN = secrets['token']
