from fastapi import HTTPException, status
from models.author import Author
from sqlalchemy.orm import Session
from models.post import Post
from schemas import author as AuthorSchemas


def create_author(data: AuthorSchemas.Author, db):
    author = Author(
        name=data.name,
        email=data.email
    )
    try:
        db.add(author)
        db.commit()
        db.refresh(author)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Ошибка при создании автора"
        )
    return author


def get_author(id: int, db):
    author = db.query(Author).filter(Author.id==id).first()
    if author:
        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Автор не найден"
    )


def get_all_authors(db):
    authors = db.query(Author).all()
    if authors:
        return authors
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Аторы не найдены"
    )


def update_author(data: AuthorSchemas.Author, db: Session, id: int):
    author = db.query(Author).filter(Author.id==id).first()
    if author:
        author.name = data.name
        author.email = data.email

        db.add(author)
        db.commit()
        db.refresh(author)

        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Автор не найден"
    )


def remove_author(id: int, db: Session):
    author = db.query(Author).filter(Author.id==id).first()
    if author:
        db.delete(author)
        db.commit()
        return True
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Автор не существует"
    )


def get_posts_by_author(author_id:int, db):
    posts = db.query(Post).filter(Post.author_id==author_id).all()
    if posts:
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Этот автор еще ничего не опубликовал"
    )