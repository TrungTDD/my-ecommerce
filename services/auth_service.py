import logging
import secrets

from core.exceptions import (
    AuthenticationError,
    ForbidenException,
    InternalException,
    InvalidInputException,
)
from models.shop_model import ShopCreateResponse, ShopLoginResponse
from models.token_model import TokenResponse
from schemas.key_token_schema import KeyTokenSchema
from schemas.shop_schema import ShopSchema
from services.shop_service import shop_service
from services.token_service import token_service
from utils.auth_utils import auth_utils
from utils.token_utils import token_utils


class AuthService:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def signup(self, *, name: str, email: str, password: str):
        self._logger.info("Start to create new shop")
        if shop_service.is_existed_email(email):
            raise InvalidInputException("Email already exists.")

        # step 2: Create new shop.
        hashed_password = auth_utils.generate_hash_password(password)
        created_shop = shop_service.insert(name, email, hashed_password)

        if not created_shop:
            self._logger.debug(f"Can not create new shop with email: {email}")
            raise InternalException(f"Can not create new shop with email: {email}")

        # step 3: Create access and refresh token for the new shop.
        self._logger.info(
            f"Start to create access and refresh token for new shop with id: {created_shop['id']}"
        )
        access_token_secret = secrets.token_hex(32)
        refresh_token_secret = secrets.token_hex(32)

        to_encode = {
            "id": str(created_shop["id"]),
            "email": email,
            "name": name,
        }

        access_token = token_utils.generate_token(
            data=to_encode, secret=access_token_secret
        )

        refresh_token = token_utils.generate_token(
            data=to_encode, secret=refresh_token_secret, expiration_time=7 * 24 * 60
        )

        token_service.insert(
            created_shop["id"],
            access_token_secret,
            refresh_token_secret,
            refresh_token,
        )

        token = TokenResponse(access_token=access_token, refresh_token=refresh_token)

        return ShopCreateResponse(
            id=str(created_shop["id"]), name=name, email=email, tokens=token
        )

    def login(self, *, email, password) -> ShopLoginResponse:
        found_shop = shop_service.find_by_email(email)

        if not auth_utils.verify_password(password, found_shop.password):
            raise AuthenticationError("Wrong password")

        encode_data = {
            "id": str(found_shop["id"]),
            "email": email,
            "name": found_shop["name"],
        }

        access_token_secret = secrets.token_hex(32)
        refresh_token_secret = secrets.token_hex(32)

        access_token = token_utils.generate_token(
            data=encode_data, secret=access_token_secret
        )

        refresh_token = token_utils.generate_token(
            data=encode_data,
            secret=refresh_token_secret,
            expiration_time=7 * 24 * 60,
        )

        token_service.update(
            found_shop["id"],
            access_token_secret,
            refresh_token_secret,
            refresh_token,
        )

        token_response = TokenResponse(
            access_token=access_token, refresh_token=refresh_token
        )
        return ShopLoginResponse(tokens=token_response)


auth_service = AuthService()
