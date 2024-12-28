from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.infrastructure.database.models.base_model import BaseModel
from datetime import datetime


class CategoryORM(BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
