from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app= FastAPI()

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

@app.get('/',response_class=HTMLResponse,include_in_schema=False)
def hello():
    return f"<h1>{posts[0]['content']}</h1>"

@app.get('/api/posts')
def get_posts():
    return posts