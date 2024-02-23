from passlib.context import CryptContext


class Crypt:
    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto", default='bcrypt')

    def verify(self, value, hashed_value):
        return self.context.verify(value, hashed_value)

    def hash(self, value):
        return self.context.hash(value)
