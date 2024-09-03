from typing import Any, Coroutine, Dict, Optional
from fastapi_pagination import Page
from sqlalchemy.ext.asyncio import AsyncSession
from .base import CRUDBase
from ..schemas.user import UserUpdate, UserCreate
from ..models.user import User

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    
    async def get(self, db: AsyncSession, obj_id: str) -> User:
        return await super().get(db, obj_id)
    
    async def get_or_create(self, db: AsyncSession, defaults: Dict[str, Any] | None, **kwargs: Any) ->  User:
        return await super().get_or_create(db, defaults, **kwargs)
    
    async def get_multi(self, db: AsyncSession, *, skip: int = 0, limit: int = 20) -> Page[User]:
        print(f"limit {limit}")
        return await super().get_multi(db, skip=skip, limit=limit)
    
    async def update(self, db: AsyncSession, *, obj_current: User, obj_new: UserUpdate | Dict[str, Any] | User):
        return await super().update(db, obj_current=obj_current, obj_new=obj_new)
    
    async def remove(self, db: AsyncSession, *, obj_id: str) -> User | None:
        return await super().remove(db, obj_id=obj_id)
    
user_crud = CRUDUser(User)