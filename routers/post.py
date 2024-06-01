from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import List

from schemas import post as PostSchemas
from controllers import post as PostControllers

router = APIRouter()


@router.post("/", tags=["post"])
async def create_post(tag_name: List[str], data: PostSchemas.Post = None, db: Session = Depends(get_db)):
    return PostControllers.create_post(data, tag_name , db)


@router.get("/{id}", tags=["post"])
async def get_post(id: int, db: Session = Depends(get_db)):
    return PostControllers.get_post(id, db)


@router.get("/", tags=["post"])
async def get_all_posts(db: Session = Depends(get_db)):
    return PostControllers.get_all_posts(db)



@router.put("/{id}", tags=["post"])
async def update_post(id: int, data: PostSchemas.Post = None, db: Session = Depends(get_db)):
    return PostControllers.update_post(data, db, id)


@router.delete("/{id}", tags=["post"])
async def remove_post(id: int, db: Session = Depends(get_db)):
    return PostControllers.remove_post(db, id)


@router.get("/tags/{post_id}", tags=["post"])
async def get_all_tags(post_id: int, db: Session = Depends(get_db)):
    return PostControllers.get_tags_by_post(post_id, db)