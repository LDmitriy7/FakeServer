from loader import app


@app.get('/')
def test():
    return {'ok': True}


@app.get('/payment')
def test():
    return {'ok': True}
