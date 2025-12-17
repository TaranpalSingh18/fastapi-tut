from pydantic import Field, BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class SignupModel(BaseModel):
    id: Optional[id]
    username: Annotated[str, Field(max_length=50)]
    email: EmailStr
    password: str
    confirm_password: str
    isStaff: Annotated[bool,Field(default=False)] 

class LoginBaseModel(BaseModel):
    username: Annotated[str, Field(max_length=50)]
    password: str

