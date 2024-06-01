from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    author_id: int
    category_id: int