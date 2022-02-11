from fastapi import APIRouter, status

from models.movie import MoviePublic

router = APIRouter()

@router.get("/{id}", status_code=status.HTTP_201_CREATED)
async def get_movie_details(id: int) -> MoviePublic:
    return MoviePublic(id=id, title="Movie", thumbnail_url="http://example.com/image.png", genres=[])