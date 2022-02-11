from pydantic import BaseModel

class UserBase(BaseModel):
  id: int

class UserCreateResponse(UserBase):
  pass

class UserPublic(UserBase):
  movies_rated_count: int

class UserDB(UserBase):
  pass