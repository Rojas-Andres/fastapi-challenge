from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.modules.category.service_layer import services
from app.modules.category.adapters.unit_of_work import CategoryUnitOfWork
from app.modules.category.domain.models import CategoryCreate

router = APIRouter()


@router.get("/")
def api_get_categorys():
    categorys = services.GetAllCategorys(uow=CategoryUnitOfWork()).get()
    return {"data": categorys}


@router.post("/")
def api_create_category(category_create: CategoryCreate):
    category = services.CreateCategory(uow=CategoryUnitOfWork()).create(
        **category_create.dict()
    )
    return {"data": category}


@router.post("/{category_id}")
def api_get_single_category(category_id: int):
    category = services.GetSingleCategory(uow=CategoryUnitOfWork()).get(category_id)
    return {"data": category}