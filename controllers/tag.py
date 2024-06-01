from fastapi import HTTPException, status
from models.tag import Tag
from models.post import Post
from models.post_tag import Post_Tag
from sqlalchemy.orm import Session
from schemas import tag as TagSchemas

def create_tag(data: TagSchemas.Tag, db):
    tag = Tag(
        name=data.name,
    )
    try:
        db.add(tag)
        db.commit()
        db.refresh(tag)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Ошибка при создании тега"
        )
    return tag


def get_tag(id: int, db):
    tag = db.query(Tag).filter(Tag.id==id).first()
    if tag:
        return tag
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Тег не найден"
    )


def get_all_tags(db):
    tags = db.query(Tag).all()
    if tags:
        return tags
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Тег не найден"
    )


def update_tag(data: TagSchemas.Tag, db: Session, id: int):
    tag = db.query(Tag).filter(Tag.id==id).first()
    if tag:
        tag.name = data.name

        db.add(tag)
        db.commit()
        db.refresh(tag)

        return tag
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Тег не найден"
    )


def remove_tag(id: int, db: Session):
    tag = db.query(Tag).filter(Tag.id==id).first()

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Тег не найден"
        )

    posts_with_tag = db.query(Post_Tag).filter(Post_Tag.tag_id==tag.id).first()
    if posts_with_tag:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Невозможно удалить тег, он связан с постом"
        )
    
    db.delete(tag)
    db.commit()
    return True


def get_post_by_tag(tag_id: int, db: Session):
    tags = db.query(Post).join(Post.tags).filter(Tag.id==tag_id).all()
    if tags:
        return tags
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Нет постов связанных с этим тегом"
    )