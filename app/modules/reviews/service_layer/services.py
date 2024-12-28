from app.modules.reviews.domain.repository import AbstractReviewsUnitOfWork
from app.core.exceptions import ObjectNotFoundException


class CreateReview:
    def __init__(self, uow: AbstractReviewsUnitOfWork):
        self.uow = uow

    def create(self, location_id: int, category_id: int) -> dict:
        with self.uow:
            if not self.uow.locations.get_location_by_id(location_id):
                raise ObjectNotFoundException("Location not found")
            if not self.uow.category.get_category_by_id(category_id):
                raise ObjectNotFoundException("Category not found")
            review = self.uow.reviews.create_review(location_id, category_id)
            self.uow.commit()
            return review