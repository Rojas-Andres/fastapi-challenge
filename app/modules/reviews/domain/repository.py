from app.modules.shared.domain.repository import SqlAlchemyUnitOfWork
from abc import ABC, abstractmethod


class AbstractCategoryRepository(ABC):
    @abstractmethod
    def get_category_by_id(self, category_id: int): ...


class AbstractLocationRepository(ABC):
    @abstractmethod
    def get_location_by_id(self, location_id: int): ...


class AbstractReviewsRepository(ABC):
    @abstractmethod
    def create_review(self, location_id: int, category_id: int): ...


class AbstractReviewsUnitOfWork(SqlAlchemyUnitOfWork):
    locations: AbstractLocationRepository
    category: AbstractCategoryRepository
    reviews: AbstractReviewsRepository

    def __enter__(self):
        self.session = self.session_factory()
        return super().__enter__()
