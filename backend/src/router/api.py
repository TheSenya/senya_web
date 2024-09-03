# Import the APIRouter class from FastAPI
from fastapi import APIRouter

# Import the 'products' router from the 'app.api.v1.endpoints' module
from ..router import user

# Create an instance of the APIRouter
router = APIRouter()

# Include the 'products' router as a sub-router under the '/products' prefix
# and assign the tag "Products" to group related API endpoints
router.include_router(user.router, prefix="/user", tags=["User"])