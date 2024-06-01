from fastapi import HTTPException, status
from models.category import Category
from sqlalchemy.orm import Session
from models.post import Post
from schemas import category as CategorySchemas


def create_category(data: CategorySchemas.Category, db):
    category = Category(
        name=data.name,
        description=data.description
    )
    try:
        db.add(category)
        db.commit()
        db.refresh(category)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Ошибка при создании категории"
        )
    return category


def get_category(id: int, db):
    category = db.query(Category).filter(Category.id==id).first()
    if category:
        return category
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Категория не найдена"
        )


def get_all_category(db):
    categories = db.query(Category).all()
    if categories:
        return categories
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Категории не найдены"
        )
    

def update_category(data: CategorySchemas.Category, db: Session, id: int):
    category = db.query(Category).filter(Category.id==id).first()
    if category:
        category.name = data.name
        category.description = data.description

        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Категория не найдена"
        )


def remove_category(id: int, db: Session):
    category = db.query(Category).filter(Category.id==id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Категория не найдена"
        )
    category_with_post = db.query(Post).filter(Post.category_id==category.id).first()
    if category_with_post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Невозможно удалить категорию, так как он связан с постом"
        )
    db.delete(category)
    db.commit()
    return category


def get_posts_by_category(category_id: int, db):
    posts = db.query(Post).filter(Post.category_id==category_id).all()
    if posts:
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Посты по данной категории отсутствуют"
    )