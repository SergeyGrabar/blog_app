import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers import post as PostRouter
from routers import category as CategoryRouter
from routers import tag as TagRouter
from routers import author as AuthorRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(PostRouter.router, prefix="/post")
app.include_router(CategoryRouter.router, prefix="/category")
app.include_router(TagRouter.router, prefix="/tag")
app.include_router(AuthorRouter.router, prefix="/author")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)