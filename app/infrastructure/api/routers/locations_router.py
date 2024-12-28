from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.modules.location.service_layer import services
from app.modules.location.adapters.unit_of_work import LocationUnitOfWork
from app.modules.location.domain.models import LocationCreate

router = APIRouter()


@router.get("/")
def api_get_locations():
    locations = services.GetAllLocations(uow=LocationUnitOfWork()).get()
    return {"data": locations}


@router.post("/")
def api_create_location(location_create: LocationCreate):
    location = services.CreateLocation(uow=LocationUnitOfWork()).create(
        **location_create.dict()
    )
    return {"data": location}
