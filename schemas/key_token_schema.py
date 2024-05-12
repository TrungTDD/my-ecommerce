from mongoengine import ListField, ObjectIdField, StringField

from schemas.base_schema import TimeStampSchema


class KeyTokenSchema(TimeStampSchema):
    user = ObjectIdField(required=True)
    access_token_secret = StringField(required=True)
    refresh_token_secret = StringField(required=True)
    refresh_token = StringField(required=True)
    refresh_tokens_used = ListField()

    meta = {"collection": "tokens", "db_alias": "shop-db-alias"}
