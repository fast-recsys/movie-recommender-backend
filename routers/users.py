"""Router API for user API"""
from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

from db import get_database
from config import Settings, get_settings
from models.mongo import get_object_id

from models.user import UserCreateResponse, UserDB, UserPublic

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(
    db: AsyncIOMotorDatabase = Depends(get_database),
    settings: Settings = Depends(get_settings),
) -> UserCreateResponse:
    """Insert a new user into Mongodb collection"""
    user_db = UserDB()
    await db[settings.mongodb_users_collection_name].insert_one(
        user_db.dict(by_alias=True)
    )
    user = await db[settings.mongodb_users_collection_name].find_one(
        {"_id": user_db.id}
    )
    return UserCreateResponse(**user)


async def get_user_or_404(
    id: ObjectId = Depends(get_object_id),
    db: AsyncIOMotorDatabase = Depends(get_database),
    settings: Settings = Depends(get_settings),
) -> UserDB:
    """Check if a user corresponding to id exists or not"""
    user = await db[settings.mongodb_users_collection_name].find_one({"_id": id})

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return UserDB(**user)


@router.get("/{id}")
async def get_user_details(user: UserDB = Depends(get_user_or_404)) -> UserPublic:
    """Get user details according to an id"""
    return UserPublic(**user.dict(by_alias=True), movies_rated_count=len(user.ratings))
