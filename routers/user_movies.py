from fastapi import APIRouter, status

from models import SaveRatingsRequest

router = APIRouter()

@router.get("/{id}/unrated")
async def get_unrated_movies(id: int):
    return { "userId": id }

@router.post("/{id}/ratings")
async def save_ratings(request: SaveRatingsRequest):
    return request

@router.get("/{id}/ratings")
async def get_ratings():
    return []

@router.get("/{id}/recommendations")
def get_recommendations_for_user(id: int):
    return { "userId": id }
