from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from schemas import category as CategorySchemas
from controllers import category as CategoryControllers

router = APIRouter()

@router.post("/", tags=["category"])
async def create_category(data: CategorySchemas.Category = None, db: Session = Depends(get_db)):
    return CategoryControllers.create_category(data, db)


@router.get("/{id}", tags=["category"])
async def get_category(id: int, db: Session = Depends(get_db)):
    return CategoryControllers.get_category(id, db)


@router.get("/", tags=["category"])
async def get_all_category(db: Session = Depends(get_db)):
    return CategoryControllers.get_all_category(db)


@router.delete("/{id}", tags=["category"])
async def remove_category(id: int, db: Session = Depends(get_db)):
    return CategoryControllers.remove_category(id, db)


@router.put("/{id}", tags=["category"])
async def update_category(id: int, data: CategorySchemas.Category = None, db: Session = Depends(get_db)):
    return CategoryControllers.update_category(data, db, id)


@router.get("/posts/{category_id}", tags=["category"])
async def get_posts_by_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryControllers.get_posts_by_category(category_id, db)