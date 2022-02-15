from fastapi import APIRouter, Depends, status
from data import get_local_movie_details, get_unrated_movie_details
from models.user import UserDB

from models.user_movies import MovieRating, MovieRatingPayload, MovieRatingPublic, MovieRatingResponse, RecommendationResponse, UnratedMoviesResponse
from routers.users import get_user_or_404

router = APIRouter()

@router.get("/{id}/unrated")
async def get_unrated_movies(
    user: UserDB = Depends(get_user_or_404)
) -> UnratedMoviesResponse:
    rated_movie_ids = list(map(lambda x: x.movie_id, user.ratings))
    movies = await get_unrated_movie_details(rated_movie_ids)
    return UnratedMoviesResponse(movies=movies)

@router.post("/{id}/ratings", status_code=status.HTTP_204_NO_CONTENT)
async def save_ratings(payload: MovieRatingPayload):
    return

@router.get("/{id}/ratings")
async def get_ratings(
    user: UserDB = Depends(get_user_or_404)
) -> MovieRatingResponse:
    
    def make_public_movie_rating(movie_rating: MovieRating) -> MovieRatingPublic:
        return MovieRatingPublic(movie=get_local_movie_details(movie_rating.movie_id), rating=movie_rating.rating)

    user_ratings = list(map(make_public_movie_rating, user.ratings))
    return MovieRatingResponse(ratings=user_ratings)

@router.get("/{id}/recommendations")
def get_recommendations_for_user(id: int) -> RecommendationResponse:
    return RecommendationResponse(recommendations=[])
