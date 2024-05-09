from mongoengine import Document, ListField, ObjectIdField, StringField


class KeyTokenSchema(Document):
    user = ObjectIdField(required=True)
    access_token_secret = StringField(required=True)
    refresh_token_secret = StringField(required=True)
    access_tokens = ListField()

    meta = {"collection": "tokens", "db_alias": "shop-db-alias"}
