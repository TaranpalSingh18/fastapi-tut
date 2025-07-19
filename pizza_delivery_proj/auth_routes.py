from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=['auth'])

@auth_router.get('/auth')
def hello():
    return {"message":"I am an Auth Route"}