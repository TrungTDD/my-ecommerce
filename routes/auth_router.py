from fastapi import APIRouter

from core.constants import StatusCode
from core.route_handler import AuthenticationRouteHandler
from db.connection import ShopConnectionDepend
from models.shop_model import (
    ShopCreateRequest,
    ShopCreateResponse,
    ShopLoginRequest,
    ShopLoginResponse,
)
from services.auth_service import auth_service

router = APIRouter()


@router.post(
    "/register", status_code=StatusCode.CREATED, response_model=ShopCreateResponse
)
def register_shop(shop_client: ShopConnectionDepend, request: ShopCreateRequest):
    response = auth_service.signup(
        name=request.name, email=request.email, password=request.password
    )
    return response


@router.post("/login", status_code=StatusCode.OK, response_model=ShopLoginResponse)
def login(shop_client: ShopConnectionDepend, request: ShopLoginRequest):
    response = auth_service.login(email=request.email, password=request.password)
    return response
