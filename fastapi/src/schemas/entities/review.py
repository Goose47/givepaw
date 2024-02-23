import datetime
from typing import Optional

from pydantic import BaseModel

from src.database import models
from src.schemas import BaseResponseSchema, User, UserShort

from src.schemas.entities.base import BaseEntityTime


class Review(BaseEntityTime):
    advertisement_id: int
    user_id: int

    text: str
    rating: int


class ReviewResponse(BaseModel, BaseResponseSchema):
    text: str
    rating: int
    user: UserShort
    created_at: datetime.datetime


class ReviewCreate(Review):
    pass


class ReviewUpdate(Review):
    pass


def create_review_response(review: models.Review, user: UserShort):
    response = ReviewResponse(
        id=review.id,
        text=review.text,
        rating=review.rating,
        user=user,
        created_at=review.created_at
    )

    return response
