from shared.database.database import Base
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, UniqueConstraint, ForeignKey, Time, Sequence, Text, CheckConstraint
from datetime import datetime


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(20))
    password = Column(String(250))
    is_active = Column(Integer,default=1)
    
    
class Cities(Base):
    __tablename__ = "Cities"
    city_id = Column(Integer, primary_key=True,autoincrement=True)
    cityname = Column(String(20))
    bestplace = Column(String(250))
    is_there = Column(Integer,default=1)
    
    
