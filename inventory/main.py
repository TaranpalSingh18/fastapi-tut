from fastapi import FastAPI
from auth_routers import auth_router
from operation_routers import op_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(op_router)

