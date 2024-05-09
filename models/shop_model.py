from pydantic import BaseModel, EmailStr

from models.token_model import TokenResponse


class ShopCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class ShopCreateResponse(BaseModel):
    name: str
    email: EmailStr
    tokens: TokenResponse
