from fastapi import APIRouter

from core.constants import StatusCode
from core.route_handler import RouteHandler
from db.connection import ShopConnectionDepend
from models.shop_model import ShopCreateRequest, ShopCreateResponse
from services.shop_service import shop_service

router = APIRouter(route_class=RouteHandler)


@router.post(
    "/register", status_code=StatusCode.CREATED, response_model=ShopCreateResponse
)
def create_shop(shop_client: ShopConnectionDepend, request: ShopCreateRequest):
    response = shop_service.signup(
        name=request.name, email=request.email, password=request.password
    )
    return response
