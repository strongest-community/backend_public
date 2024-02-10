from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from api.schemas.user import UserCreate
from api.models.models import User
from api.auth.hash import Hash


async def create_user(db: AsyncSession, request: UserCreate):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.get_password_hash(request.password),
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_username(db: AsyncSession, username: int):
    stmt = select(User).where(User.username == id)
    result = await db.execute(stmt)
    user = result.scalars().first()

    if not username:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {username} not found",
        )
    return user
