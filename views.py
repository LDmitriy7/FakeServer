from typing import Optional

from fastapi import HTTPException, responses, status, Response, Request, Header
# from fastapi.middleware.cors import CORSMiddleware

import config
from loader import app
from models import documents, models


# origins = [
#     "https://my-bots.ru",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get('/go/{rule_key}')
def go_rule_by_key(response: Response, rule_key: str):
    go_rule_doc: documents.GoRule = documents.GoRule.objects(key=rule_key).first()

    if go_rule_doc is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    # response.headers['Referer-policy'] = 'origin'

    return responses.RedirectResponse(go_rule_doc.url, headers={'Referer-policy': 'origin'})


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
    print(url)
    return responses.RedirectResponse(url)
