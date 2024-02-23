from fastapi import APIRouter

from src.api.responses.api_response import ApiResponse
from src.database.models import Review
from src.repository.crud import review_repository
from src.schemas import create_user_short, create_review_response

router = APIRouter(
    prefix="/review",
    tags=["review"],

)


@router.get(path='/{review_id}')
async def get_review(review_id: int):
    try:
        review: Review = await review_repository.get_single(id=review_id)
        if review is None:
            raise Exception("No review with this id")
    except Exception as e:
        return ApiResponse.error(str(e))
    user = create_user_short(review.user)

    result: dict = create_review_response(review, user).jsonify()
    return ApiResponse.payload(result)
