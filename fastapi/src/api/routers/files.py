from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import FileResponse
from src.api.dependencies.auth import Auth
from src.config.app.config import settings_app

router = APIRouter(
    prefix="/files",
    tags=["files"],
)


@router.get('/assets/{path}')
async def get_file(path: str):
    try:
        image_path = settings_app.APP_PATH + '/storage/assets/' + path
        return FileResponse(image_path)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail={"cause": e.with_traceback})
