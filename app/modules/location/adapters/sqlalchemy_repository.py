from app.modules.location.domain.repository import AbstractLocationRepository
from app.infrastructure.database.models import LocationORM
from sqlalchemy.orm import Session


class LocationSqlAlchemyRepository(AbstractLocationRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_locations(self):
        return self.session.query(LocationORM).all()

    def create_location(self):
        location = LocationORM(name="Test 2", latitude=0.0, longitude=0.0)
        self.session.add(location)
