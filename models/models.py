from pydantic import BaseModel


class GoRule(BaseModel):
    key: str
    url: str
