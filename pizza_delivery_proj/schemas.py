from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import List, Dict, Annotated, Optional

class SignupModel(BaseModel):
    id:Optional[int]
    username:Annotated[str, Field(max_length=25)]
    email: EmailStr
    password:SecretStr
    isStaff:Annotated[bool, Field(default=False)]
    isActive:Annotated[bool, Field(default=False)]
