from database import Base, engine
from models import Order, Base

Base.metadata.create_all(bind=engine)