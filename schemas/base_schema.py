from datetime import datetime

from mongoengine import DateTimeField, Document


class TimeStampSchema(Document):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    meta = {"abstract": True}
