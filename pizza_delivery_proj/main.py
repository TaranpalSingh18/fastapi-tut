from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)


@AuthJWT.load_config
def get_config():
    return Settings()

@app.get('/')
def home():
    return({"message":"this is my home page"})

