from fastapi.routing import APIRouter

auth_router = APIRouter(prefix="/auth")

@auth_router.get('/signup')
async def signup():
    
