from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from schemas import tag as TagSchemas
from controllers import tag as TagControllers

router = APIRouter()

@router.post("/", tags=["tag"])
async def create_tag(data: TagSchemas.Tag = None, db: Session = Depends(get_db)):
    return TagControllers.create_tag(data, db)


@router.get("/{id}", tags=["tag"])
async def get_tag(id: int, db: Session = Depends(get_db)):
    return TagControllers.get_tag(id, db)


@router.get("/", tags=["tag"])
async def get_all_tag(db: Session = Depends(get_db)):
    return TagControllers.get_all_tags(db)


@router.delete("/{id}", tags=["tag"])
async def remove_tag(id: int, db: Session = Depends(get_db)):
    return TagControllers.remove_tag(id, db)


@router.put("/{id}", tags=["tag"])
async def update_tag(id: int, data: TagSchemas.Tag, db: Session = Depends(get_db)):
    return TagControllers.update_tag(data, db, id)


@router.get("/posts/{tag_id}", tags=["tag"])
async def get_posts_by_tag(tag_id: int, db: Session = Depends(get_db)):
    return TagControllers.get_post_by_tag(tag_id, db)