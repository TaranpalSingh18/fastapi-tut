from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine= create_engine("postgresql://postgres:taran1234@localhost/pizza-delivery", echo=True)

Base = declarative_base()
Session = sessionmaker()

