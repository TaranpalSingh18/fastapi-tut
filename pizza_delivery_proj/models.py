from database import Base
from database import Session
from sqlalchemy import Column, Boolean, Text, Integer, String, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="user"
    id=Column(Integer, primary_key=True)
    username=Column(String(25), unique=True)
    email=Column(String(50), unique=True)
    password=Column(Text, nullable=False)
    isStaff=Column(Boolean, default=False)
    isActive = Column(Boolean, default=False)
    order=relationship('Orders', back_populates="user")

    def __repr__(self):
        return f"<User : {self.username}>"
    
class Order(Base):

    ORDER_STATUSES=(
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'transit'),
        ('DELIVERED', 'delivered')
    )

    PIZZA_SIZES=(
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA-LARGE","extra-large")
    )

    __tablename__="choice"
    id=Column(Integer, primary_key=True)
    quantity=Column(Integer, nullable=False)
    choice_type=Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")


    __tablename__="Orders"
    id=Column(Integer, primary_key=True)
    quantity=Column(Integer, nullable=False)
    choice_type=Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size= Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")
    user_id= Column(Integer, ForeignKey("user.id"))
    user = relationship("user", back_populates="Orders")


    def __repr__(self):
        return f"ID is {self.id}>"



