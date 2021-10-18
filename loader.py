import mongoengine as me
from fastapi import FastAPI

import config

app = FastAPI()

me.connect(
    db=config.Database.NAME,
    host=config.Database.HOST,
    port=config.Database.PORT,
    username=config.Database.USERNAME,
    password=config.Database.PASSWORD,
    authentication_source=config.Database.AUTH_SOURCE,
)
