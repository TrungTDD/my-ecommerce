import enum
from datetime import datetime

from mongoengine import (
    BooleanField,
    DateTimeField,
    Document,
    EmailField,
    EnumField,
    ListField,
    StringField,
)

from schemas.base_schema import TimeStampSchema


class StatusEnum(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class ShopSchema(TimeStampSchema):
    name = StringField(max_length=150, required=True)
    email = EmailField(max_length=255, unique=True, required=True)
    password = StringField(required=True)
    status = EnumField(enum=StatusEnum, default=StatusEnum.ACTIVE)
    verify = BooleanField(default=False)
    roles = ListField()

    meta = {"collection": "shops", "db_alias": "shop-db-alias"}
