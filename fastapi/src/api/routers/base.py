from fastapi import FastAPI

from src.api.routers import mock_routes, auth


def create_routes(app: FastAPI):
    app.include_router(auth.router)
    app.include_router(mock_routes.router)
    return app
