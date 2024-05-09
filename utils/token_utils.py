from datetime import datetime, timedelta

from jose import jwt

TOKEN_EXPIRED_MINUTES = 3 * 60 * 24
ALGORITHM = "HS256"


class TokenUtils:
    def generate_token(
        self,
        data: dict,
        secret: str,
        algorithm: str = ALGORITHM,
        expiration_time: int = TOKEN_EXPIRED_MINUTES,
    ) -> str:
        """Generate a token from the given secret.

        Args:
            data (dict): Encoded data.
            secret (str): Secret to generate the token.
            algorithm (str, optional): Algorithm uses to generate token . Defaults to 'HS256'.
            expiration_time (int, optional): Expiration time of the token. Defaults to 3 days.

        Returns:
            str: Generated token.
        """
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=expiration_time)
        to_encode.update({"exp": expire})
        token_encoded = jwt.encode(to_encode, secret, algorithm=algorithm)
        return token_encoded


token_utils = TokenUtils()
