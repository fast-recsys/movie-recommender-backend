from typing import List
from pydantic import BaseModel, Field
from models.mongo import MongoBaseModel, PyObjectId

from models.user_movies import MovieRating

class UserBase(BaseModel):
  id: str

class UserCreateResponse(UserBase):
  pass

class UserDB(MongoBaseModel):
  ratings: List[MovieRating] = Field(default_factory=list)


class UserPublic(UserBase):
  movies_rated_count: int

  @classmethod
  def from_userdb(cls, user_db: UserDB):
    return UserPublic(id=str(user_db.id), movies_rated_count=len(user_db.ratings))