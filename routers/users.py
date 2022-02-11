from fastapi import APIRouter, status

from models.user import UserCreateResponse, UserPublic

router = APIRouter()

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user() -> UserCreateResponse:
    return UserCreateResponse(id=42)

@router.get("/{id}")
async def get_user_details(id: int) -> UserPublic:
    return UserPublic(id=id, movies_rated_count=0)
