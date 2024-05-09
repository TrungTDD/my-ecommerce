from bson.objectid import ObjectId

from core.exceptions import DBErrorException
from schemas.key_token_schema import KeyTokenSchema


class TokenService:
    def __init__(self) -> None:
        pass

    def insert(
        self, user_id: ObjectId, access_token_secret: str, refresh_token_secret: str
    ) -> str:
        """Insert new token into token schema.

        Args:
            user_id (ObjectId): Id of the user
            access_token_secret (str): Secret of the access token.
            refresh_token_secret (str): Secret of the refresh token.

        Raises:
            DBErrorException: Can't insert new token.

        Returns:
            str: Inserted id of new token.
        """
        created_token = KeyTokenSchema(
            user=user_id,
            access_token_secret=access_token_secret,
            refresh_token_secret=refresh_token_secret,
        ).save()

        if not created_token:
            raise DBErrorException("Can not insert token.")

        return str(created_token["id"])


token_service = TokenService()
