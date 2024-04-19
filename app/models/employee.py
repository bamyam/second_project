from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True) # 아이디
    name = Column(String(20), nullable=False)               # 이름
    job_position = Column(String(50), nullable=False)       # 직급
    department_name = Column(String(50), nullable=False)    # 부서명
    phone_number = Column(String(13), nullable=False)       # 전화번호
    email = Column(String(150), nullable=False)             # 이메일
    security_grade = Column(Integer, nullable=False)        # 보안등급(1,2,3) 3등급이 가장 낮은 등급
