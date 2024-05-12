from fastapi import APIRouter

from routes import shop_router

router = APIRouter()


@router.get("/")
def hello():
    return {"hello": "world"}


router.include_router(shop_router.router, prefix="/shop", tags="shop")
