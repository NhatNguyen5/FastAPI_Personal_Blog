from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ntnlog import Logger, Level

app = FastAPI()
home_logger = Logger(colorize=True, name="home_log", level="TRACE")
post_logger = Logger(colorize=True, name="post_log")

posts: list[dict] = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    home_logger.enable_log_tracing(True)
    home_logger("Called from home")
    home_logger("Called from home", "TRACE", "")
    home_logger("Called from home", "WARN", "")
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    post_logger.enable_log_tracing(True)
    post_logger("Called from get_posts", "WARN", console_message="")
    post_logger.enable_log_tracing(False)
    post_logger("Called from get_posts", "INFO", console_message="")
    return posts

