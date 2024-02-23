
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base


class AdvertisementAdTag(Base):
    __tablename__ = "advertisement__ad_tag"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)

    ad_tag_id: Mapped[int] = mapped_column(ForeignKey("ad_tag.id"), nullable=False, primary_key=True)
