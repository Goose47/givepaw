from fastapi import FastAPI

from src.api.routers import mock_routes, auth, pets


def create_routes(app: FastAPI):
    app.include_router(auth.router)
    app.include_router(mock_routes.router)
    app.include_router(pets.router)
    return app
