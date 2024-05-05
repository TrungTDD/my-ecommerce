from fastapi import APIRouter

from routes import shop_router

router = APIRouter()

router.include_router(shop_router.router, prefix="/shop", tags="shop")
