from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ApiResponse(BaseModel):
    @staticmethod
    def success(message: str = 'OK'):
        return JSONResponse(
            content=ApiResponse.format_content(message=message),
            status_code=200,
        )

    @staticmethod
    def payload(data: dict):
        return JSONResponse(
            content=ApiResponse.format_content(data=data),
            status_code=200,
        )

    @staticmethod
    def error(message: str = 'An error has occurred', status_code: int = 400):
        return JSONResponse(
            content=ApiResponse.format_content(message=message),
            status_code=status_code,
        )

    @staticmethod
    def errors(errors: dict, status_code: int = 400):
        return JSONResponse(
            content=ApiResponse.format_content(errors=errors),
            status_code=status_code,
        )

    @staticmethod
    def format_content(message=None, data=None, errors=None):
        content = {}

        if message:
            content['detail'] = message
        if data:
            content['data'] = data
        if errors:
            content['errors'] = errors

        return content
