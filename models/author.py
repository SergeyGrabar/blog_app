from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    posts = relationship("Post", back_populates="author", uselist=True, cascade="all, delete")

    