from fastapi import FastAPI

from app.routers.users import router as user_router
from app.routers.movies import router as movie_router
from app.routers.user_movies import router as user_movies_router

app = FastAPI()

@app.get("/")
def health_check():
    return "The server is alive..."

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(movie_router, prefix="/movies", tags=["movies"])
app.include_router(user_movies_router, prefix="/users", tags=["user movies"])
