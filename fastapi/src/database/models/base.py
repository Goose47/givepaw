from sqlalchemy.orm import mapped_column, Mapped, declarative_base

Base = declarative_base()


class AbstractModel(Base):
    __abstract__ = True
    extend_existing = True

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
