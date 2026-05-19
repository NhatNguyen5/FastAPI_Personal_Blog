from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ntnlog import Logger

app = FastAPI()
app_logger = Logger()

posts: list[dict] = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    app_logger.log("Called from home")
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    app_logger.log("Called from get_posts")
    return posts

