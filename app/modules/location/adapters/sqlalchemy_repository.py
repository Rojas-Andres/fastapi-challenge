from app.modules.location.domain.repository import AbstractLocationRepository
from app.infrastructure.database.models import LocationORM
from sqlalchemy.orm import Session


class LocationSqlAlchemyRepository(AbstractLocationRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_locations(self) -> list[dict]:
        return [
            self.to_dict(location) for location in self.session.query(LocationORM).all()
        ]

    def create_location(self, name: str, latitude: float, longitude: float) -> dict:
        location = LocationORM(name=name, latitude=latitude, longitude=longitude)
        self.session.add(location)
        self.session.flush()
        return self.to_dict(location)

    def to_dict(self, location: LocationORM) -> dict:
        return {
            "id": location.id,
            "name": location.name,
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
