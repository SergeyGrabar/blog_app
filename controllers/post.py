from fastapi import HTTPException, status
from models.post import Post
from models.tag import Tag
from models.post_tag import Post_Tag
from sqlalchemy.orm import Session
from schemas import post as PostSchema
from typing import List


def create_post(data: PostSchema.Post, tag_names: List[str], db: Session):
    try:
        post = Post(
            title=data.title,
            content=data.content,
            author_id=data.author_id,
            category_id=data.category_id
        )
        db.add(post)
        db.commit()
        db.refresh(post)
        
        for tag_name in tag_names:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
                db.commit()
                db.refresh(tag)
            post_tag = Post_Tag(post_id=post.id, tag_id=tag.id)
            db.add(post_tag)
            db.commit()
            db.refresh(post_tag)

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Ошибка при создании поста"
        )
    return post


def get_post(id: int, db):
    post = db.query(Post).filter(Post.id==id).first()
    if post:
        return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Пост не найден"
    )


def get_all_posts(db):
    posts = db.query(Post).all()
    if posts:
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Пост не найден"
    )


def update_post(data: PostSchema.Post, db: Session, id: int):
    post = db.query(Post).filter(Post.id==id).first()
    if post:
        post.title = data.title
        post.content = data.content
        post.author_id = data.author_id
        post.category_id = data.category_id

        db.add(post)
        db.commit()
        db.refresh(post)

        return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Пост не найден"
    )


def remove_post(db: Session, id: int):
    post = db.query(Post).filter(Post.id==id)
    if post.first():
        post.delete()
        db.commit()
        return True
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Пост не найден"
    )


def get_tags_by_post(post_id: int, db: Session):
    tags = db.query(Tag).join(Tag.posts).filter(Post.id==post_id).all()
    if tags:
        return tags
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Нет тегов связанных с этим постом"
    )