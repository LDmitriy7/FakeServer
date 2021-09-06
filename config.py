import toml

env = toml.load('env.toml')

HOST = env['HOST']
PORT = env['PORT']
SSL_CERTFILE = env['SSL_CERTFILE']
SSL_KEYFILE = env['SSL_KEYFILE']
TOKEN = env['TOKEN']
