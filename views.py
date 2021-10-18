from typing import Optional

from fastapi import HTTPException, responses, status, Request, Header

import api
import config
from loader import app
from models import documents, models


@app.get('/test')
def test():
    content = api.render_template('redirect.html', redirect_url='https://www.web-api.eu/myreferer/')
    return responses.HTMLResponse(content)


@app.get('/go/{rule_key}')
def go_rule_by_key(rule_key: str):
    go_rule_doc: documents.GoRule = documents.GoRule.objects(key=rule_key).first()

    if go_rule_doc is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    content = api.render_template('redirect.html', redirect_url=go_rule_doc.url)
    return responses.HTMLResponse(content)


@app.post('/go')
def add_go_rule(request: Request, go_rule: models.GoRule, token: Optional[str] = Header(None)):
    if token != config.Secrets.TOKEN:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    go_rule_doc: documents.GoRule = documents.GoRule.objects(key=go_rule.key).first()

    if go_rule_doc:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail='This key already exists')

    documents.GoRule(**go_rule.dict()).save()

    return {'new_url': request.url_for('go_rule_by_key', key=go_rule.key)}


@app.get('/go')
def go(url: str):
    content = api.render_template('redirect.html', redirect_url=url)
    return responses.HTMLResponse(content)
