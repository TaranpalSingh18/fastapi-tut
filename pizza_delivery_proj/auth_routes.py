from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import SignupModel
from models import User
from werkzeug.security import generate_password_hash

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
async def login(payload: SignupModel):
    session = Session(bind=engine)
    try:
        db_email=session.query(User).filter(User.email==payload.email).first()
        db_username=session.query(User).filter(User.username==payload.username).first()

        if db_email is None:
            raise HTTPException(status_code=404,detail="No Email ID exists! Signup and make one!")
        if db_username is None:
            raise HTTPException(status_code=404, detail="No Username exists! Make one")
        
        return JSONResponse(status_code=200, content="Login Succesfull")

    finally:
        session.close()

