from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import SignupModel, LoginModel
from models import User
from fastapi_jwt_auth import AuthJWT
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(prefix="/auth", tags=['auth'])


@auth_router.post('/signup')
async def signup(payload: SignupModel):
    session = Session(bind=engine)
    try:
        db_email = session.query(User).filter(User.email == payload.email).first()
        db_username = session.query(User).filter(User.username == payload.username).first()

        if db_email is not None:
            raise HTTPException(status_code=400, detail="Email already exists. Please login.")

        if db_username is not None:
            raise HTTPException(status_code=400, detail="Username already taken.")

        new_user = User(
            username=payload.username,
            email=payload.email,
            password=generate_password_hash(payload.password.get_secret_value()),
            isStaff=payload.isStaff,
            isActive=payload.isActive
        )

        session.add(new_user)
        session.commit()

        return JSONResponse(status_code=201, content={"message": "New user created successfully."})
    finally:
        session.close()


@auth_router.post('/login')
async def loginRoute(payload: LoginModel, Authorize: AuthJWT=Depends()):
    session = Session(bind=engine)
    
    db_user = session.query(User).filter(User.username == payload.username).first()
        
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
            
    if not check_password_hash(db_user.password, payload.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = Authorize.create_access_token(subject=db_user.username)
    refresh_token = Authorize.create_refresh_token(subject=db_user.username)

    response = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

    return jsonable_encoder(response)
    

    



    