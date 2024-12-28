from app.modules.reviews.domain.repository import AbstractReviewsUnitOfWork
from app.core.exceptions import ObjectNotFoundException


class CreateReview:
    def __init__(self, uow: AbstractReviewsUnitOfWork):
        self.uow = uow

    def create(self, location_id: int, category_id: int):
        with self.uow:
            location_id = self.uow.locations.get_location_by_id(location_id)
            if not location_id:
                raise ObjectNotFoundException("Location not found")
            category_id = self.uow.category.get_category_by_id(category_id)
            if not category_id:
                raise ObjectNotFoundException("Category not found")
