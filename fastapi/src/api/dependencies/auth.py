from fastapi import Request, HTTPException
from jose import JWTError
from typing import Optional

from src.repository.crud.entities.user import user_repo
from src.database.models.entities.user import User
from src.utils.jwt.jwt_auth import JWT
from src.utils.jwt.token_type import TokenType
from src.config.jwt.config import settings_jwt


class Auth:
    def __init__(self):
        self.user: Optional[User] = None
        self.jwt: JWT = JWT(settings_jwt)

    async def check_access_token(self, request: Request):
        access_token = request.cookies.get('jwt_access_token')
        if access_token is None:
            raise HTTPException(detail='Access token is not present', status_code=401)
        _, user = await self.check_token(access_token, TokenType.ACCESS)
        request.state.user = user

    async def check_refresh_token(self, request: Request):
        refresh_token = request.cookies.get('jwt_refresh_token')
        if refresh_token is None:
            raise HTTPException(detail='Refresh token is not present', status_code=401)
        payload, _ = await self.check_token(refresh_token, TokenType.REFRESH)
        return payload

    async def check_token(self, token, type):
        try:
            payload = self.jwt.verify_token(token)
        except JWTError:
            self.raise_credentials_exception()

        if payload['type'] != type:
            self.raise_credentials_exception()

        email: str = payload['sub']
        if email is None:
            self.raise_credentials_exception()
        user: User = await user_repo.get_single(email=email)
        if user is None:
            self.raise_credentials_exception()

        return payload, user

    def raise_credentials_exception(self):
        raise HTTPException(
            status_code=401,
            detail="Unauthenticated",
        )
