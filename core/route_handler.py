import logging
import traceback
from typing import Callable

from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response

from core.exceptions import (
    AuthenticationError,
    BaseException,
    InternalException,
)

logger = logging.getLogger(__name__)


class AuthenticationRouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            jwt_token = request.headers.get("Authorization")
            if not jwt_token:
                raise AuthenticationError("Invalid jwt token")

            try:
                response = await original_route_handler(request)
                return response
            except BaseException as e:
                logger.error(traceback.format_exc())
                raise e
            except Exception as e:
                # catch unexpected exceptions
                logger.error(traceback.format_exc())
                raise InternalException(str(e))

        return custom_route_handler
