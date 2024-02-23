from typing import List

from sqlalchemy.orm import relationship, Mapped

from src.database.models.characteristics.base import AbstractCharacteristicModel


class TransactionType(AbstractCharacteristicModel):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

    __tablename__ = "transaction_type"

    transactions: Mapped[List["Transaction"]] = relationship(back_populates="transaction_type", uselist=True,
                                                             lazy="selectin")

    def __repr__(self) -> str:
        return f"TransactionType(id={self.id}, title={self.title})"
