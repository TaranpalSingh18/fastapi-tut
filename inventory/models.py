from database import Base
from sqlalchemy import Boolean, String, Integer, Text, ForeignKey, Column
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User (Base):
    __tablename__="user"

    id= Column(Integer, primary_key=True)
    username= Column(String(25), unique=True)
    email= Column(String)
    password= Column(String)
    confirm_password= Column(String)
    isStaff= Column(Boolean)


