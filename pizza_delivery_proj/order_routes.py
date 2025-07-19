from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=['order'])

@order_router.get('/order')
def hello_man():
    return {"message":"this is an order router"}