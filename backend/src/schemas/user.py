from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str  # Name of the User (required)
    password: str  # password of the User (required)

    
class UserCreate(UserBase):
    ...
    
class UserUpdate(UserBase):
    ...
    
class UserPatch(UserBase):
    name: Optional[str]   # Name is optional for patching
    price: Optional[str]  # Price is optional for patching

class User(UserBase):
    id: str
        
    class Config:
        orm_mode = True