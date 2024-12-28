from app.modules.shared.domain.repository import SqlAlchemyUnitOfWork
from abc import ABC, abstractmethod


class AbstractLocationRepository(ABC):
    @abstractmethod
    def get_locations(self):
        raise NotImplementedError

    @abstractmethod
    def create_location(self):
        raise NotImplementedError


class AbstractLocationUnitOfWork(SqlAlchemyUnitOfWork):
    location: AbstractLocationRepository

    def __enter__(self):
        self.session = self.session_factory()
        return super().__enter__()
