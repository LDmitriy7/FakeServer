import mongoengine as me


class GoRule(me.Document):
    key: str = me.StringField()
    url: str = me.StringField()
