from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.infrastructure.database.models.base_model import BaseModel
from datetime import datetime
from sqlalchemy.orm import relationship


class LocationCategoryReviewORM(BaseModel):
    __tablename__ = "location_category_reviews"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    reviewed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    location = relationship("LocationORM", back_populates="reviews")
    category = relationship("CategoryORM", back_populates="reviews")