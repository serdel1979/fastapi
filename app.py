from fastapi import FastAPI

app = FastAPI()

posts = []

@app.get('/')
def read_root():
    return{"welcome":"soy un REST api con fastapi"}

@app.get('/posts')
def get_posts():
    return posts