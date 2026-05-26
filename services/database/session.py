from collections.abc import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from services.database.engine import engine


async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


async def get_database_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


async def check_database_connection() -> bool:
    try:
        async with async_session_factory() as session:
            await session.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
