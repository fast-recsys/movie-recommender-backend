from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException

from app.data import get_movie_details
from app.models.movie import MoviePublic

router = APIRouter()


@router.get("/{id}")
async def get_movie_details(
    movie: Optional[MoviePublic] = Depends(get_movie_details),
) -> MoviePublic:
    """Corresponding to an id get the movie details"""
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return movie
