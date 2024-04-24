from pydantic import BaseModel
from datetime import datetime

class Visitors(BaseModel):
    name: str
    company_name: str
    email: str
    department_name: str
    job_position: str
    phone_number: str
    employee_id: str
    purpose: str
    location_id: str
    status: str
    regdate: datetime
    visit_date: str

    class Config:
        from_attributes = True