from fastapi.routing import APIRouter

op_router = APIRouter(prefix="/op")

@op_router.get('/crud')
def crud_op():
    return {"message":"this is a crud op"}