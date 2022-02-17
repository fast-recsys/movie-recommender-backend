from fastapi import APIRouter, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models.user import UserDB
from app.models.user_movies import (
    MovieRating,
    MovieRatingPayload,
    MovieRatingPublic,
    MovieRatingResponse,
    RecommendationResponse,
    UnratedMoviesResponse,
)
from app.routers.users import get_user_or_404
from app.data import get_local_movie_details, get_unrated_movie_details
from app.db import get_database
from app.config import Settings, get_settings

router = APIRouter()


@router.get("/{id}/unrated")
async def get_unrated_movies(
    user: UserDB = Depends(get_user_or_404),
) -> UnratedMoviesResponse:
    rated_movie_ids = list(map(lambda x: x.movie_id, user.ratings))
    movies = await get_unrated_movie_details(rated_movie_ids)
    return UnratedMoviesResponse(movies=movies)


@router.post("/{id}/ratings", status_code=status.HTTP_204_NO_CONTENT)
async def save_ratings(
    payload: MovieRatingPayload,
    user: UserDB = Depends(get_user_or_404),
    db: AsyncIOMotorDatabase = Depends(get_database),
    settings: Settings = Depends(get_settings),
) -> None:

    user_ratings = list(map(lambda x: x.dict(), payload.ratings))

    await db[settings.mongodb_users_collection_name].update_one(
        {"_id": user.id}, {"$push": {"ratings": {"$each": user_ratings}}}
    )


@router.get("/{id}/ratings")
async def get_ratings(user: UserDB = Depends(get_user_or_404)) -> MovieRatingResponse:
    def make_public_movie_rating(movie_rating: MovieRating) -> MovieRatingPublic:
        return MovieRatingPublic(
            movie=get_local_movie_details(movie_rating.movie_id),
            rating=movie_rating.rating,
        )

    user_ratings = list(map(make_public_movie_rating, user.ratings))
    return MovieRatingResponse(ratings=user_ratings)


@router.get("/{id}/recommendations")
def get_recommendations_for_user(id: int) -> RecommendationResponse:
    return RecommendationResponse(recommendations=[])
