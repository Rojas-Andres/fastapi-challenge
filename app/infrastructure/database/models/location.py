from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.infrastructure.database.models.base_model import BaseModel
from datetime import datetime
from sqlalchemy.orm import relationship


class LocationORM(BaseModel):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("LocationCategoryReviewORM", back_populates="location")
