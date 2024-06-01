from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from schemas import author as AuthorSchemas
from controllers import author as AuthorControllers

router = APIRouter()

@router.post("/", tags=["author"])
async def create_author(data: AuthorSchemas.Author = None, db: Session = Depends(get_db)):
    return AuthorControllers.create_author(data, db)


@router.delete("/{id}", tags=["author"])
async def remove_author(id: int, db: Session = Depends(get_db)):
    return AuthorControllers.remove_author(id, db)


@router.put("/{id}", tags=["author"])
async def update_author(id: int, data: AuthorSchemas.Author = None, db: Session = Depends(get_db)):
    return AuthorControllers.update_author(data, db, id)


@router.get("/{id}", tags=["author"])
async def get_author(id: int, db: Session = Depends(get_db)):
    return AuthorControllers.get_author(id, db)


@router.get("/authors/", tags=["author"])
async def get_all_authors(db: Session = Depends(get_db)):
    return AuthorControllers.get_all_authors(db)


@router.get("/posts/{author_id}", tags=["author"])
async def get_posts_by_author(author_id: int, db: Session = Depends(get_db)):
    return AuthorControllers.get_posts_by_author(author_id, db)