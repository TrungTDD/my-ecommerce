from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.route_handler import AuthenticationRouteHandler
from routes import auth_router

reusable_oauth2 = HTTPBearer(scheme_name="Authorization")
router = APIRouter(route_class=AuthenticationRouteHandler)


@router.get("/")
def hello():
    return {"hello": "world"}


router.include_router(
    auth_router.router,
    prefix="/auth",
    tags="auth",
    dependencies=[Depends(reusable_oauth2)],
)
