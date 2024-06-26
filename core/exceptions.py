from fastapi.exceptions import HTTPException


class BaseException(HTTPException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code=status_code, detail=message)


class BadRequestException(BaseException):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(status_code, message)


class ForbidenException(BaseException):
    def __init__(self, message: str, status_code: int = 403):
        super().__init__(status_code, message)


class AuthenticationError(BaseException):
    def __init__(self, message: str, status_code: int = 401):
        super().__init__(status_code, message)


class ObjectNotFoundException(BaseException):
    def __init__(self, message: str, status_code: int = 404):
        super().__init__(status_code, message)


class InvalidInputException(BaseException):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(status_code, message)


class DBErrorException(BaseException):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(status_code, message)


class InternalException(BaseException):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(status_code, message)
