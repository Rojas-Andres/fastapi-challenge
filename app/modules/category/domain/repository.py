from app.modules.shared.domain.repository import SqlAlchemyUnitOfWork
from abc import ABC, abstractmethod


class AbstractCategoryRepository(ABC):
    @abstractmethod
    def get_categorys(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def create_category(self, name: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_category_by_id(self, Category_id: int) -> dict:
        raise NotImplementedError


class AbstractCategoryUnitOfWork(SqlAlchemyUnitOfWork):
    category: AbstractCategoryRepository

    def __enter__(self):
        self.session = self.session_factory()
        return super().__enter__()
