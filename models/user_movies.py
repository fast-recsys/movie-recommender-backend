from typing import List
from pydantic import BaseModel, Field
from models.movie import MovieBase, MoviePublic

# Response for unrated movies

class UnratedMoviesResponse(BaseModel):
  movies: List[MoviePublic]


# Payload for saving movie ratings

class MovieRating(BaseModel):
  movie_id: int
  rating: int = Field(..., ge=1, le=5)

class MovieRatingPayload(BaseModel):
  ratings: List[MovieRating]


# Response for getting rated movies

class MovieRatingPublic(BaseModel):
  movie: MovieBase
  rating: int = Field(..., ge=1, le=5)

class MovieRatingResponse(BaseModel):
  ratings: List[MovieRatingPublic]


# Response for recommendations

class MovieRecommendation(BaseModel):
  movie: MoviePublic
  match: float = Field(..., ge=0, le=1)

class RecommendationResponse(BaseModel):
  recommendations: List[MovieRecommendation]