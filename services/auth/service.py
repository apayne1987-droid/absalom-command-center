from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.auth.schemas.auth import UserRegisterRequest
from services.auth.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from services.database.models.user import User


async def register_user(
    session: AsyncSession,
    payload: UserRegisterRequest,
) -> User:
    existing_user = await session.scalar(
        select(User).where(User.email == payload.email)
    )

    if existing_user:
        raise ValueError("User already exists")

    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )

    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user


async def authenticate_user(
    session: AsyncSession,
    email: str,
    password: str,
) -> str | None:
    user = await session.scalar(
        select(User).where(User.email == email)
    )

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return create_access_token(user.email)
