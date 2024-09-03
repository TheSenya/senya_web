from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from .db_session import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        yield db