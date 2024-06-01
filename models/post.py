from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.author import Author
from models.category import Category
from models.post_tag import Post_Tag


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(String, default=datetime.now(timezone.utc))

    author = relationship("Author", back_populates="posts", uselist=False)
    category = relationship("Category", back_populates="posts", uselist=False)

    tags = relationship("Tag", secondary="posts_tags", back_populates="posts", uselist=True)