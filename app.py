import uvicorn

import config
from views import app

__all__ = ['app']

if __name__ == '__main__':
    uvicorn.run(
        f'{__name__}:app',
        host=config.App.HOST,
        port=config.App.PORT,
        ssl_certfile=config.SSL.CERTFILE,
        ssl_keyfile=config.SSL.KEYFILE,
    )
