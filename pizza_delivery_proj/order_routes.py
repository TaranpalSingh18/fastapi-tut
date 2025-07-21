from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from models import User, Order
from schemas import OrderModel, Settings
from database import Session, engine
from fastapi.responses import JSONResponse

order_router = APIRouter(prefix="/order", tags=['order'])

session = Session(bind = engine)


@order_router.get('/')
def authorization(Authorize: AuthJWT=Depends()):
    try:
        AuthJWT.jwt_required()
        
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized Request/Token Invalid")
    

@order_router.post('/orders')
async def placeOrder(payload: OrderModel, Authorise: AuthJWT = Depends()):
    try:
        Authorise.jwt_required()  # ✅ Call on the injected instance
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized Request/Token Invalid")
    
    current_user = Authorise.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()

    if user is not None:
        new_order = Order(
            quantity=payload.quantity,
            pizza_size=payload.pizza_size,
            choice_type=payload.choice_type
        )
        new_order.user = user
        session.add(new_order)
        session.commit()  # ✅ Missing in your code (very important)
        
        return JSONResponse(status_code=200, content={"order": {
            "id": new_order.id,
            "quantity": new_order.quantity,
            "pizza_size": new_order.pizza_size,
            "choice_type": new_order.choice_type
        }})
    
    else:
        raise HTTPException(status_code=404, detail="User Not Found!")


    
    
    
