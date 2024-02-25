from fastapi import FastAPI

from src.api.routers import mock_routes, auth, pets, cities, blood_groups, donors, recipients, clinics, users, files, user_networks, respond, blood_bank


def create_routes(app: FastAPI):
    app.include_router(auth.router)
    app.include_router(mock_routes.router)
    app.include_router(pets.router)
    app.include_router(cities.router)
    app.include_router(blood_groups.router)
    app.include_router(donors.router)
    app.include_router(recipients.router)
    app.include_router(clinics.router)
    app.include_router(users.router)
    app.include_router(files.router)
    app.include_router(user_networks.router)
    app.include_router(respond.router)
    app.include_router(blood_bank.router)

    return app
