import mongoengine as me
import uvicorn
from fastapi import FastAPI, HTTPException, responses, Request, status
from pydantic import BaseModel

import config

me.connect(
    db=config.Database.NAME,
    host=config.Database.HOST,
    port=config.Database.PORT,
    username=config.Database.USERNAME,
    password=config.Database.PASSWORD,
    authentication_source=config.Database.AUTH_SOURCE,
)

app = FastAPI()


class RedirectRule(BaseModel):
    key: str
    url: str


class RedirectRuleDoc(me.Document):
    key: str = me.StringField()
    url: str = me.StringField()


@app.get('/redirect/{key}')
def do_redirect(key: str):
    redirect_rule_doc: RedirectRuleDoc = RedirectRuleDoc.objects(key=key).first()
    if redirect_rule_doc is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return responses.RedirectResponse(redirect_rule_doc.url)


@app.post('/redirect')
def add_redirect_rule(request: Request, redirect_rule: RedirectRule, token: str):
    if token != config.Secrets.TOKEN:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    redirect_rule_doc: RedirectRuleDoc = RedirectRuleDoc.objects(key=redirect_rule.key).first()

    if redirect_rule_doc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail='This key already exists')

    RedirectRuleDoc(**redirect_rule.dict()).save()

    return {'short_url': request.url_for('do_redirect', key=redirect_rule.key)}


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=config.App.HOST,
        port=config.App.PORT,
        ssl_certfile=config.SSL.CERTFILE,
        ssl_keyfile=config.SSL.KEYFILE,
    )
