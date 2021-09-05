import ssl

from aiohttp import web

import config

app = web.Application()


async def index(_request: web.Request):
    return web.Response(text='Hello, world')


app.router.add_get('/', index)

ssl_context = ssl.SSLContext()
ssl_context.load_cert_chain(config.CERT_FILE, config.KEY_FILE)

web.run_app(app, host=config.HOST, port=config.PORT, ssl_context=ssl_context)
