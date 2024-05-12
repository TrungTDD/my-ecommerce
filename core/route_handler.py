from typing import Any, Callable, Coroutine

from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response


class RouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                response = await original_route_handler(request)
                return response
            except (RequestValidationError, HTTPException) as e:
                raise e

        return custom_route_handler
