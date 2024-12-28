from app.modules.reviews.domain.repository import (
    AbstractReviewsRepository,
    AbstractCategoryRepository,
    AbstractLocationRepository,
)
from app.infrastructure.database.models import LocationORM, CategoryORM
from sqlalchemy.orm import Session


class ReviewsSqlAlchemyRepository(AbstractReviewsRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def create_review(self, location_id: int, category_id: int): ...


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
