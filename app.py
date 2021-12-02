from typing import Text, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

posts = []

#modelo de un Post 

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published = bool = False



@app.get('/')
def read_root():
    return{"welcome":"soy un REST api con fastapi"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id:str):
    for p in posts:
        if p['id'] == post_id:
            return p
    raise HTTPException(status_code=404, detail = "No encontrado")

@app.delete("/posts/{post_id}")
def delete_post(post_id):
    for index,post in enumerate(posts):
       if post["id"] == post_id:
           posts.pop(index)
           return {"message": "La publicacion se eliminó"}
    return "No encontrado"

@app.put("/posts/{post_id}")
def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"]= updatePost.title
            posts[index]["content"]= updatePost.content
            posts[index]["author"]= updatePost.author
            return {"message": "La publicacion se editó"}
    raise HTTPException(status_code=404, detail = "No encontrado")
        


