from fastapi.responses import RedirectResponse

import config
from loader import app


@app.get('/')
def test():
    return {'ok': True}


@app.get('/payment')
def test():
    return {'ok': True}


@app.get('/redirect')
def test():
    return RedirectResponse(config.REDIRECT_TO)
