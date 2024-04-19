from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True) # PK
    location = Column(String(100), nullable=False)      # 이름
    security_grade = Column(Integer, nullable=False)    # 보안등급(1,2,3) 3등급이 가장 낮은 등급
