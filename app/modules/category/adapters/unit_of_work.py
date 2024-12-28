from app.modules.category.domain.repository import AbstractCategoryUnitOfWork
from app.modules.category.adapters.sqlalchemy_repository import (
    CategorySqlAlchemyRepository,
)


class CategoryUnitOfWork(AbstractCategoryUnitOfWork):
    def __enter__(self):
        super().__enter__()
        self.category = CategorySqlAlchemyRepository(self.session)
