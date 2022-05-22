import uvicorn

import config
from views import app

__all__ = ['app']

if __name__ == '__main__':
    uvicorn.run(
        f'{__name__}:app',
        host=config.APP_HOST,
        port=config.APP_PORT,
        ssl_certfile=config.SSL_CERTFILE,
        ssl_keyfile=config.SSL_KEYFILE,
    )
