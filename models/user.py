from typing import List
from pydantic import BaseModel, Field
from models.mongo import MongoBaseModel, PyObjectId

from models.user_movies import MovieRating

class UserBase(MongoBaseModel):
  pass

class UserCreateResponse(UserBase):
  pass

class UserDB(MongoBaseModel):
  ratings: List[MovieRating] = Field(default_factory=list)


class UserPublic(MongoBaseModel):
  movies_rated_count: int
