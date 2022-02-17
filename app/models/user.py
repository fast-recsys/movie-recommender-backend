from typing import List
from pydantic import BaseModel, Field
from app.models.mongo import MongoBaseModel, PyObjectId

from app.models.user_movies import MovieRating

class UserBase(MongoBaseModel):
  pass

class UserCreateResponse(UserBase):
  pass

class UserDB(MongoBaseModel):
  ratings: List[MovieRating] = Field(default_factory=list)


class UserPublic(MongoBaseModel):
  movies_rated_count: int
