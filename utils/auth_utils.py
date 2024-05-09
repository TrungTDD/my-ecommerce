from passlib.context import CryptContext


class AuthUtils:
    def __init__(self) -> None:
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def generate_hash_password(self, password: str) -> str:
        """Generate a hash password.

        Args:
            password (str): Raw password of the user.

        Returns:
            str: Hashed password.
        """
        return self._pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify the password against the hashed password.

        Args:
            plain_password (str): Plain password.
            hashed_password (str): Hashed password.

        Returns:
            bool: Whether the plain password is correct.
        """
        return self._pwd_context.verify(plain_password, hashed_password)


auth_utils = AuthUtils()
