from app.modules.reviews.domain.repository import (
    AbstractReviewsRepository,
    AbstractCategoryRepository,
    AbstractLocationRepository,
)
from app.infrastructure.database.models import (
    LocationORM,
    CategoryORM,
    LocationCategoryReviewORM,
)
from sqlalchemy.orm import Session


class ReviewsSqlAlchemyRepository(AbstractReviewsRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def create_review(self, location_id: int, category_id: int) -> dict:
        review = LocationCategoryReviewORM(
            location_id=location_id, category_id=category_id
        )
        self.session.add(review)
        self.session.flush()
        return self.to_dict(review)

    def to_dict(self, review: LocationCategoryReviewORM) -> dict:
        return {
            "id": review.id,
            "location_id": review.location_id,
            "category_id": review.category_id,
        }


class CategorySqlAlchemyRepository(AbstractCategoryRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_category_by_id(self, category_id: int):
        return self.session.query(CategoryORM).filter_by(id=category_id).first()


class LocationSqlAlchemyRepository(AbstractLocationRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_location_by_id(self, location_id: int):
        return self.session.query(LocationORM).filter_by(id=location_id).first()
