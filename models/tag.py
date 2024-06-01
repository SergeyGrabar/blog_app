from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    posts = relationship("Post", secondary="posts_tags", back_populates="tags")