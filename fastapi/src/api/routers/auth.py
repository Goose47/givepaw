from fastapi import APIRouter, Depends, Request, HTTPException, UploadFile, Form
from fastapi.responses import JSONResponse
from http import HTTPStatus

from src.api.dependencies.auth import Auth
from src.api.use_cases.auth import *
from src.schemas.auth import *

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
# async def register(user: RegisterUser):
async def register(avatar: Optional[UploadFile] = None, user: RegisterUser = Depends(RegisterUser.as_form)):
    try:
        registered_user: UserType = await RegisterUseCase.register(user, avatar)
        access_token, refresh_token, user = await LoginUseCase.login(
            LoginUser(username=user.username, password=user.password))
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
    return format_jwt_response(access_token, refresh_token, registered_user)


@router.post("/login")
async def login(user: LoginUser):
    try:
        access_token, refresh_token, user = await LoginUseCase.login(user)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))

    return format_jwt_response(access_token, refresh_token, UserType(
        id=user.id,
        username=user.username,
        name=user.name,
        surname=user.surname,
        patronymic=user.patronymic,
        email=user.email,
        user_role_id=user.user_role_id,
        city_id=user.city_id,
        avatar_id=user.avatar_id
    ))


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
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)

    return format_jwt_response(access_token, refresh_token)


def format_jwt_response(access_token: str, refresh_token: str, user=None):
    response = JSONResponse(
        content={
            'user': dict(user) if user else None
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
