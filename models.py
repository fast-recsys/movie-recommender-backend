from pydantic import BaseModel
from typing import List

class UserRating(BaseModel):
    movie_id: int
    rating: int

class RecommendationRequest(BaseModel):
    user_ratings: List[UserRating]

class Movie(BaseModel):
    movie_id: int
    imdb_id: str