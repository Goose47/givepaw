from typing import Any
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from src.utils.jwt.token_type import TokenType


class JWT:
    def __init__(self, config) -> None:
        self._config = config

    def generate_access_token(self, subject: str, payload: dict[str, Any] = {}) -> str:
        return self.__sign_token(
            type=TokenType.ACCESS.value,
            subject=subject,
            payload=payload,
            ttl=self._config.ACCESS_TOKEN_TTL,
        )

    def generate_refresh_token(self, subject: str, payload: dict[str, Any] = {}) -> str:
        return self.__sign_token(
            type=TokenType.REFRESH.value,
            subject=subject,
            payload=payload,
            ttl=self._config.REFRESH_TOKEN_TTL,
        )

    def __sign_token(self, type: str, subject: str, payload: dict[str, Any] = {}, ttl: int = None) -> str:
        now = datetime.now(timezone.utc).timestamp()

        data = {
            'sub': subject,
            'type': type,
            'iat': now,
        }
        data.update({'exp': now + int(timedelta(minutes=ttl).total_seconds())}) if ttl else None
        payload.update(data)

        return jwt.encode(data, self._config.JWT_SECRET_KEY, algorithm=self._config.JWT_ALGORITHM)

    def verify_token(self, token) -> dict[str, Any]:
        return jwt.decode(token, self._config.JWT_SECRET_KEY, algorithms=[self._config.JWT_ALGORITHM])

    def get_jti(self, token) -> str:
        return self.verify_token(token)['jti']

    def get_sub(self, token) -> str:
        return self.verify_token(token)['sub']

    def get_exp(self, token) -> int:
        return self.verify_token(token)['exp']
