# from pydantic import BaseModel, EmailStr, AnyUrl, Field, SecretStr
# from typing import List, Dict, Annotated

# class User(BaseModel):
#     id: str
#     username: Annotated[str, Field(max_length=50)]
#     email: EmailStr
#     password: SecretStr
#     isStaff: Annotated[bool, Field(default=False)]
#     isActive: Annotated[bool, Field(default=False)]

# def validated_user(object: User):
#     return {"User":object.username}


# class Choice(BaseModel):
    


# class Order(BaseModel):
#     id: str
#     quantity: int
#     order_status: str
#     pizza_size: str
#     flavour: str
#     user_id: str
