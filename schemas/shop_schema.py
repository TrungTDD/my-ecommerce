import enum
from datetime import datetime

from mongoengine import (
    DateTimeField,
    Document,
    EmailField,
    EnumField,
    ListField,
    StringField,
)


class StatusEnum(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class ShopSchema(Document):
    name = StringField(max_length=150, required=True)
    email = EmailField(max_length=255, unique=True, required=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    status = EnumField(enum=StatusEnum, default=StatusEnum.ACTIVE)
    roles = ListField()
    meta = {"collection": "shop_collection", "db_alias": "shop-db-alias"}
