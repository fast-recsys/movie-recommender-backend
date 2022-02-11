from fastapi import APIRouter, status

router = APIRouter()

@router.get("/{id}", status_code=status.HTTP_201_CREATED)
async def get_movie_details(id: int):
    return { "movieId": id }