from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from http import HTTPStatus

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.use_cases.auth import *
from src.database.models import User
from src.schemas.auth import *


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=RegisterUser)
async def register(user: RegisterUser):
    try:
        user: User = await RegisterUseCase.register(user)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
    return user


@router.post("/login")
async def login(user: LoginUser):
    try:
        access_token, refresh_token = await LoginUseCase.login(user)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))

    return format_jwt_response(access_token, refresh_token)


@router.post("/logout")
async def logout(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    #  todo revoke token cause unsetting it is not enough??
    response = JSONResponse(content='You have successfully logged out.')
    response.delete_cookie('jwt_access_token')
    response.delete_cookie('jwt_refresh_token')
    return response


@router.post('/refresh')
async def refresh(request: Request, auth: Auth = Depends()):
    payload = await auth.check_refresh_token(request)  # todo dto for payload
    try:
        access_token, refresh_token = await RefreshUseCase.refresh(payload)
    except Exception as e:
        return ApiResponse.error(str(e), 401)

    return format_jwt_response(access_token, refresh_token)


def format_jwt_response(access_token: str, refresh_token: str):
    response = JSONResponse(
        content={
            'access_token': access_token,
            'refresh_token': refresh_token,
        },
        status_code=HTTPStatus.OK
    )

    response.set_cookie(
        key="jwt_access_token",
        value=access_token,
        httponly=True,
    )
    response.set_cookie(
        key="jwt_refresh_token",
        value=refresh_token,
        httponly=True,
    )

    return response
