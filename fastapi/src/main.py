
from fastapi import Request
import uvicorn
from fastapi import FastAPI


from src.admin.base import setup_admin
from src.api.responses.api_response import ApiResponse
from src.api.routers import auth, advertisement, review
from src.config.app.config import settings_app
from src.database.session_manager import db_manager
from src.utils.validator.exceptions import AppValidationException


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings_app.APP_NAME,
        debug=settings_app.DEBUG,
        version=settings_app.APP_VERSION
    )

    return application


app = get_application()

admin = setup_admin(app, db_manager.engine)

app.include_router(auth.router)
app.include_router(advertisement.router)
app.include_router(review.router)


@app.exception_handler(AppValidationException)
async def validation_failed(request: Request, exc: AppValidationException):
    return ApiResponse.errors(exc.errors, status_code=422)


if __name__ == "__main__":
    uvicorn.run(
        app=settings_app.UVICORN_APP_NAME,
        host=settings_app.UVICORN_HOST,
        port=settings_app.UVICORN_PORT,
        reload=settings_app.UVICORN_RELOAD
    )
