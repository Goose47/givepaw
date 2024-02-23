from fastapi import Request
import uvicorn
from fastapi import FastAPI

from src.api.responses.api_response import ApiResponse
from src.api.routers.base import create_routes
from src.config.app.config import settings_app
from src.utils.validator.exceptions import AppValidationException


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings_app.APP_NAME,
        debug=settings_app.DEBUG,
        version=settings_app.APP_VERSION
    )

    application = create_routes(application)
    return application


app = get_application()

"""
@app.exception_handler(AppValidationException)
async def validation_failed(request: Request, exc: AppValidationException):
    return ApiResponse.errors(exc.errors, status_code=422)
"""

if __name__ == "__main__":
    uvicorn.run(
        app=settings_app.UVICORN_APP_NAME,
        host=settings_app.UVICORN_HOST,
        port=settings_app.UVICORN_PORT,
        reload=settings_app.UVICORN_RELOAD
    )
