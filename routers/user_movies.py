from fastapi import APIRouter, status

from models.user_movies import MovieRatingPayload, MovieRatingResponse, RecommendationResponse, UnratedMoviesResponse

router = APIRouter()

@router.get("/{id}/unrated")
async def get_unrated_movies(id: int) -> UnratedMoviesResponse:
    return UnratedMoviesResponse(movies=[])

@router.post("/{id}/ratings", status_code=status.HTTP_204_NO_CONTENT)
async def save_ratings(payload: MovieRatingPayload):
    return

@router.get("/{id}/ratings")
async def get_ratings(id: int) -> MovieRatingResponse:
    return MovieRatingResponse(ratings=[])

@router.get("/{id}/recommendations")
def get_recommendations_for_user(id: int) -> RecommendationResponse:
    return RecommendationResponse(recommendations=[])
