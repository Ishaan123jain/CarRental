from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    name = Column(String, index=True)
    email = Column(String, index=True, nullable=False)
    username = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)

class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    days = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
