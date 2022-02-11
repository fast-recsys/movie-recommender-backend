from typing import List
from pydantic import BaseModel, HttpUrl

class MovieBase(BaseModel):
  id: int
  title: str

class MoviePublic(MovieBase):
  thumbnail_url: HttpUrl
  genres: List[str]

