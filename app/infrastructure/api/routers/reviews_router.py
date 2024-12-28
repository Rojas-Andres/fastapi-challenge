from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.modules.reviews.service_layer import services
from app.modules.reviews.adapters.unit_of_work import ReviewsUnitOfWork
from app.modules.reviews.domain.models import ReviewCreate
from app.modules.location.adapters.unit_of_work import LocationUnitOfWork

router = APIRouter()


@router.post("/")
def api_create_review(review_create: ReviewCreate):
    review_create = services.CreateReview(uow=ReviewsUnitOfWork()).create(
        **review_create.dict()
    )
    return {"data": review_create}
