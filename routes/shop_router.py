from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from mongoengine.errors import ValidationError

from db.connection import ShopConnectionDepend
from schemas.shop_schema import ShopSchema

router = APIRouter()


@router.get("/")
def get_shop(shop_client: ShopConnectionDepend):
    try:
        shop = ShopSchema(
            name="test shop",
            email="trungtdd@aagmail.com",
            password="123123",
            roles=["advcs"],
        )
        shop.save()
    except ValidationError as e:
        print(e)
        raise HTTPException(400, e.message)
    return {"Hello": "World"}
