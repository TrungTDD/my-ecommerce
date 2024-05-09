import logging
import secrets

from mongoengine.errors import NotUniqueError, ValidationError

from core.exceptions import BadRequestException
from models.shop_model import ShopCreateResponse
from models.token_model import TokenResponse
from schemas.shop_schema import ShopSchema
from services.token_service import token_service
from utils.auth_utils import auth_utils
from utils.token_utils import token_utils


class ShopService:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def signup(self, *, name: str, email: str, password: str):
        try:
            self._logger.info("Start to create new shop")
            # step 1: Check whether the email already exists.
            shop = ShopSchema.objects(email=email).first()
            if shop:
                raise BadRequestException(f"Email: {email} is already exists")

            # step 2: Create new shop.
            hashed_password = auth_utils.generate_hash_password(password)
            shop = ShopSchema(
                name=name,
                email=email,
                password=hashed_password,
            )
            created_shop = shop.save()
            if not created_shop:
                self._logger.debug(f"Can not create new shop with email: {email}")
                raise BadRequestException(
                    f"Can not create new shop with email: {email}"
                )

            self._logger.debug(
                f"Create new shop successfully with id: {created_shop['id']}"
            )

        except ValidationError as e:
            self._logger.error(f"Validation error while create new shop: {e}")
            raise BadRequestException(e.message)

        # step 3: Create access and refresh token for the new shop.
        self._logger.info(
            f"Start to create access and refresh token for new shop with id: {created_shop['id']}"
        )
        access_token_secret = secrets.token_hex(32)
        refresh_token_secret = secrets.token_hex(32)
        token_service.insert(
            created_shop["id"], access_token_secret, refresh_token_secret
        )

        to_encode = {"id": str(created_shop["id"]), "email": email, "name": name}

        access_token = token_utils.generate_token(
            data=to_encode, secret=access_token_secret
        )

        refresh_token = token_utils.generate_token(
            data=to_encode, secret=refresh_token_secret, expiration_time=7 * 24 * 60
        )

        token = TokenResponse(access_token=access_token, refresh_token=refresh_token)

        return ShopCreateResponse(name=name, email=email, tokens=token)


shop_service = ShopService()
