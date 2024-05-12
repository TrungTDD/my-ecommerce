import logging

from core.exceptions import ObjectNotFoundException
from schemas.shop_schema import ShopSchema


class ShopService:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def find_by_email(self, email):
        shop = ShopSchema.objects(email=email).first()
        if not shop:
            raise ObjectNotFoundException("Email does not exist")
        return shop

    def is_existed_email(self, email):
        shop = ShopSchema.objects(email=email).first()
        return shop is not None

    def insert(self, name, email, password):
        return ShopSchema(
            name=name,
            email=email,
            password=password,
        ).save()


shop_service = ShopService()
