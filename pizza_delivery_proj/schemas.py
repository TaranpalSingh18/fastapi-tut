from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import List, Dict, Annotated, Optional

class SignupModel(BaseModel):
    id: Optional[int]
    username: str = Field(max_length=25)
    email: EmailStr
    password: SecretStr
    isStaff: bool = Field(default=False)
    isActive: bool = Field(default=False)



class Settings(BaseModel):
    authjwt_secret_key:str="5ae5de81638dbca5c446ed52feed72f0aee915ecb9b771528a87738a1b42d44f"

class LoginModel(BaseModel):
    username:str
    password: str


class OrderModel(BaseModel):
    id: Optional[str]
    quantity: int
    choice_type: Optional[str]="PENDING"
    pizza_size : Optional[str]="SMALL"
    user_id:Optional[int]

class orderStatus(BaseModel):
    status : Optional[str]
