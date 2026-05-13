from fastapi import FastAPI,Request,HTTPException,status
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app= FastAPI()

app.mount("/static",StaticFiles(directory="static"), name="static")
templates= Jinja2Templates(directory='templates')

posts : list[dict] = [
    {
        "id":1,
        "author":"Yash Raj",
        "title":"World Famous Lover",
        "content":"Love has no limits,one who truly loves you will never hesitate to help you.",
        "date_posted":"May 13, 2026"
    },
    {
        "id":2,
        "author":"Keerthana",
        "title":"I Don't Care ",
        "content":"You can't force yourself to love someone, for whom you doesn't have any feeling, you want him just as your friend.",
        "date_posted":"May 11, 2026"
    }
]

@app.get('/',include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"Home Page"})

@app.get('/api/posts')
def get_posts():
    return posts

@app.get('/{id}')
def get_post_id(id:int):
    for post in posts:
        if post["id"]==id:
            return post
    # return {"message":"post not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")