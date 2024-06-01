from database import Base
from sqlalchemy import Column, Integer, ForeignKey


class Post_Tag(Base):
    __tablename__ = "posts_tags"

    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)