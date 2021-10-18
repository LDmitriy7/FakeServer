import toml

_env = toml.load('env.toml')


class App:
    _data = _env['App']

    HOST = _data['HOST']
    PORT = _data['PORT']


class SSL:
    _data = _env['SSL']

    CERTFILE = _data.get('CERTFILE')
    KEYFILE = _data.get('KEYFILE')


class Database:
    _data = _env['Database']

    NAME = _data['NAME']
    HOST = _data.get('HOST')
    PORT = _data.get('PORT')
    USERNAME = _data.get('USERNAME')
    PASSWORD = _data.get('PASSWORD')
    AUTH_SOURCE = _data.get('AUTH_SOURCE', 'admin')


class Secrets:
    _data = _env['Secrets']

    TOKEN = _data['TOKEN']
