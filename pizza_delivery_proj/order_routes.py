from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from models import User, Order
from schemas import OrderModel, Settings
from database import Session, engine
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


order_router = APIRouter(prefix="/order", tags=['order'])

session = Session(bind = engine)


@order_router.get('/')
def authorization(Authorize: AuthJWT=Depends()):
    try:
        AuthJWT.jwt_required()
        
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized Request/Token Invalid")
    

@order_router.post('/order')
async def placeOrder(payload: OrderModel, Authorise: AuthJWT = Depends()):
    try:
        Authorise.jwt_required()
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
        session.commit()  
        
        return JSONResponse(status_code=200, content={"order": {
            "id": new_order.id,
            "quantity": new_order.quantity,
            "pizza_size": new_order.pizza_size,
            "choice_type": new_order.choice_type
        }})
    
    else:
        raise HTTPException(status_code=404, detail="User Not Found!")
    

#for super user only
@order_router.get('/orders')
async def get_all_orders(payload: OrderModel, Authorise: AuthJWT=Depends()):
    try:
        Authorise.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorised access")
    
    current_user = Authorise.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()
    if user.isStaff:
        all_orders = session.query(Order).all()

        return JSONResponse(status_code=200, content={"All Orders are": all_orders})
    
    raise HTTPException(status_code=404, detail="User Not Found/User is not a superuser")

#for superuser only
@order_router.get('/orders/{id}')
async def get_order_by_id(id:int, Authorise: AuthJWT=Depends()):
    try: 
        Authorise.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    current_user = Authorise.get_jwt_subject()
    user = session.query(User).filter(User.username==current_user).first()

    if user.isStaff:
        order=session.query(Order).filter(Order.id==id)
        return JSONResponse(status_code=200, content={"Here's your order": order})

    else:
        return JSONResponse(status_code=401, content="Unauthorised access")
    
# for superuser only
@order_router.get('/user/orders')
async def get_all_orders_of_a_user(Authorise: AuthJWT=Depends()):
    try:
        Authorise.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    current_user = Authorise.get_jwt_subject()
    user = session.query(User).filter(User.username==current_user)
    #hence here we found our user
    return JSONResponse(status_code=200, contnet={"message":user.orders})


@order_router.get('/user/order/{order_id}')
async def get_specific_order(order_id: int, Authorise:AuthJWT=Depends()):
    try:
        Authorise.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=404, detail="Invalid Token")
    current_user = Authorise.get_jwt_subject
    user = session.query(User).filter(User.username == current_user)
    #my current user is user
    order = user.orders

    for i in order:
        if order_id == i.id:
            return JSONResponse(status_code=200, content={"message":i})
        
    raise HTTPException(status_code=404,detail="No such order found")


@order_router.put('/order/update/{order_id}')
async def update_order(id: int,orderObject: OrderModel,Authorise: AuthJWT=Depends()):
    try:
        Authorise.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=404, detail="Invalid Token")
    
    order_to_update = session.query(Order).filter(Order.id == id).first()

    order_to_update.quantity= orderObject.quantity
    order_to_update.choice_type= orderObject.choice_type
    order_to_update.pizza_size=orderObject.pizza_size

    session.commit()
    
    return jsonable_encoder(order_to_update)











    
    
    
