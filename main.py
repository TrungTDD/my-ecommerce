from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

from core.exceptions import InternalException
from routes import main

app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    message, status_code = ["Bad Request", 404]
    return JSONResponse(
        status_code=int(status_code),
        content={"detail": message},
    )


@app.middleware("http")
def test_middleware(request: Request, call_next):
    print(request.headers)
    import time

    start_time = time.time()
    response = call_next(request)
    process_time = time.time()
    print("Processing time: ", process_time - start_time)
    return response


app.include_router(main.router, prefix="/api/v1")
