from fastapi import FastAPI
from models import RecommendationRequest, UserRating
from data import get_movies

app = FastAPI()

@app.get("/")
def health_check():
    return "The server is alive..."

@app.get("/movies")
def handle_get_movies(shuffle: bool = False, limit: int = 3):
    return get_movies(limit, shuffle)

@app.post("/recommend")
def handle_get_recommendations(request: RecommendationRequest):
    user_id = 999
    return request
