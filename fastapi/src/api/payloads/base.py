

class BasePayload:
    @classmethod
    def get_fields(cls):
        return [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]

    def init(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        return self
