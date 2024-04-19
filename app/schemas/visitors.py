from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Visitors(Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 번호
    name = Column(String(20), nullable=True)                    # 방문객 이름
    company_name = Column(String(100), nullable=False)          # 회사 이름
    email = Column(String(150), nullable=False)                 # 이메일
    department_name = Column(String(50), nullable=False)        # 부서명
    job_position = Column(String(50), nullable=False)           # 직급
    phone_number = Column(String(13), nullable=False)           # 전화번호
    employee_name = Column(String(20), ForeignKey('employee.Name'))    # 담당자 이름
    purpose = Column(String(500), nullable=False)           # 방문 목적
    location = Column(String(100), ForeignKey('location.Location'), nullable=False)  # 방문 장소
    status = Column(String(1), default='N', nullable=False),            # 승인 상태(Y: 승인, N: 접수, R: 거절)
    regdate = Column(DateTime, default=datetime.now(), nullable=True)   # 신청일

