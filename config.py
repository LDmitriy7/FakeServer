import toml

env = toml.load('env.toml')

HOST = env['HOST']
PORT = env['PORT']
CERT_FILE = env['CERT_FILE']
KEY_FILE = env['KEY_FILE']
