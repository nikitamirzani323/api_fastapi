from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    return {'data':{'nama': 'Budi'}}

@app.get("/about")
async def about():
    return {'data':{'about page'}}

@app.get("/blog")
async def index(limit=10,published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog list'}
    else:
        return {'data': f'{limit} unpublished blog list'}

@app.get("/blog/unpublished")
async def unpublished():
    return {'data':{'all unpublished blog'}}

@app.get("/blog/{id}")
async def show(id: int):
    return {'data':id}

@app.get("/blog/{id}/comments")
async def comments(id, limit=10):
    return {'data': {1,2}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
async def create_blog(blog: Blog):
    return {'data': f'blog is created title as {blog.title}'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)