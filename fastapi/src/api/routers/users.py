from http import HTTPStatus

from fastapi import APIRouter, Depends, Request, HTTPException

from src.api.dependencies.auth import Auth
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import user
from src.schemas.location import Region, City
from src.schemas.user import UserRole, Avatar, UserNetwork, UserConfig

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get('/user/info', response_model=user.UserProfile)
async def get_user_info(request: Request, auth: Auth = Depends()):
    try:
        await auth.check_access_token(request)
        user_id = request.state.user.id
        user_info: models.User = await SqlAlchemyRepository(db_manager.get_session, model=models.User).get_single(

            id=user_id)

        user_role = UserRole(id=user_info.user_role.id, title=user_info.user_role.title)

        region = Region(id=user_info.city.region.id, title=user_info.city.region.title)
        city = City(id=user_info.city.id, title=user_info.city.title, region=region)

        avatar = Avatar(id=user_info.avatar.id, photo_path=user_info.avatar.photo_path,
                        photo_thumb=user_info.avatar.photo_thumb) if user_info.avatar else user_info.avatar

        user_network = UserNetwork(id=user_info.user_network.id, telegram=user_info.user_network.telegram,
                                   vk=user_info.user_network.vk)

        user_config = UserConfig(id=user_info.user_config.id,
                                 phone_number_status=user_info.user_config.phone_number_status,
                                 social_networks_status=user_info.user_config.social_networks_status,
                                 email_status=user_info.user_config.email_status)

        return user.UserProfile(id=user_info.id, surname=user_info.surname, name=user_info.name,
                                patronymic=user_info.patronymic, username=user_info.username,
                                email=user_info.email, user_role=user_role, city=city, avatar=avatar,
                                user_network=user_network, user_config=user_config)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
