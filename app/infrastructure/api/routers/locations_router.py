from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.modules.location.service_layer import services
from app.modules.location.adapters.unit_of_work import LocationUnitOfWork
# from app.interfaces.api.schemas import LocationCreate, LocationRead
# from app.application.services.location_service import LocationService

router = APIRouter()

# @router.post("/", response_model=LocationRead, status_code=status.HTTP_201_CREATED)
# def api_create_location(location: LocationCreate, service: LocationService = Depends()):
#     # loc = Location(id=0, name=location.name, latitude=location.latitude, longitude=location.longitude)
#     try:
#         created = service.add_location(loc)
#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
#     return created


@router.get("/")
def api_get_locations():
    locations = services.GetAllLocations(uow=LocationUnitOfWork()).get()
    return {"message": "Get all locations"}


@router.post("/")
def api_create_location():
    locations = services.CreateLocation(uow=LocationUnitOfWork()).create()
    return {"message": "Get all locations"}
