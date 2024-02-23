from ..base import BasePayload


class LoginPayload(BasePayload):
    email: str
    password: str
