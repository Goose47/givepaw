from src.database.models.base import AbstractModel


class AbstractBaseTransactionModel(AbstractModel):
    __abstract__ = True
