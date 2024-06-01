from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    posts = relationship("Post", back_populates="category", uselist=True, cascade="all, delete")