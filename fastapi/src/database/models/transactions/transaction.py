from typing import Optional
from fastapi import Request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.transactions.base import AbstractBaseTransactionModel


class Transaction(AbstractBaseTransactionModel):
    __tablename__ = "transaction"

    transaction_type_id: Mapped[int] = mapped_column(
        ForeignKey("transaction_type.id"), nullable=False)  # бронирование, объявление, ...
    transaction_type: Mapped["TransactionType"] = relationship(back_populates="transactions", uselist=False,
                                                               lazy="selectin")

    remote_id: Mapped[Optional[str]] = mapped_column(nullable=False)

    advertisement_id: Mapped[Optional[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="transactions", uselist=False, lazy="selectin")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
