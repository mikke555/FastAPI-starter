from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.database_url, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession | None]:
    async with SessionLocal() as session:
        yield session


if __name__ == "__main__":
    import asyncio
    from sqlalchemy import text

    async def test_db():
        async with SessionLocal() as session:
            result = await session.execute(text("SELECT 1"))
            return result.scalar()

    print(asyncio.run(test_db()))
