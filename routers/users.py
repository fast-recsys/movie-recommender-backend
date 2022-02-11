from fastapi import APIRouter, status

router = APIRouter()

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user():
    return "New User Created"

@router.get("/{id}")
async def get_user_details(id: int):
    return f"Details for user {id}"
