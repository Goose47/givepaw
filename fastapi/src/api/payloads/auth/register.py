from ..base import BasePayload


class RegisterPayload(BasePayload):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    user_status_id: int
    # avatar_id: int
