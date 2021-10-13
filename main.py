from fastapi import FastAPI
from models import RecommendationRequest, UserRating

app = FastAPI()

@app.get("/")
def health_check():
    return "The server is alive..."

@app.post("/recommend")
def get_recommendations(request: RecommendationRequest):
    user_id = 999
    return request
