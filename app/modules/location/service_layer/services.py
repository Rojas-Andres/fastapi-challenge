from app.modules.location.domain.repository import AbstractLocationUnitOfWork


class GetAllLocations:
    def __init__(
        self,
        uow: AbstractLocationUnitOfWork,
    ):
        self.uow = uow

    def get(self):
        with self.uow:
            locations = self.uow.location.get_locations()
            print(locations)
            raise ValueError("Not implemented")


class CreateLocation:
    def __init__(
        self,
        uow: AbstractLocationUnitOfWork,
    ):
        self.uow = uow

    def create(self):
        with self.uow:
            new_location = self.uow.location.create_location()
            self.uow.commit()
