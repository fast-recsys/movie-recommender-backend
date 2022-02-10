from fastapi import FastAPI, status
from models import SaveRatingsRequest, UserRating

app = FastAPI()

@app.get("/")
def health_check():
    return "The server is alive..."

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user():
    return

@app.get("/users/{id}/unrated")
async def get_unrated_movies(id: int):
    return { "userId": id }

@app.get("/movies/{id}")
async def get_movie_details(id: int):
    return { "movieId": id }

@app.post("/users/{id}/ratings")
async def save_ratings(request: SaveRatingsRequest):
    return request

@app.get("/users/{id}/ratings")
async def get_ratings():
    return

@app.post("/users/{id}/recommendations")
def get_recommendations_for_user(id: int):
    return { "userId": id }
