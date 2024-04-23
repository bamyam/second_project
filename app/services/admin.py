from sqlalchemy import update, select

from app.dbfactory import Session
from app.models.visitors import Visitors, Employee, Location

class AdminService:
    @staticmethod
    def select_visit():
        with Session() as sess:
            stmt = select(Visitors.id, Visitors.regdate, Visitors.company_name, Visitors.department_name, Visitors.job_position,
                          Visitors.name, Visitors.phone_number, Employee.department_name, Employee.job_position, Employee.name,
                          Employee.security_grade, Visitors.purpose, Location.location, Location.security_grade, Visitors.visit_date, Visitors.status)\
            .join_from(Visitors, Employee)\
            .join_from(Visitors, Location)
            result = sess.execute(stmt)

        return result

    @staticmethod
    def accept_visit(number):
        with Session() as sess:
            stmt = update(Visitors).where(Visitors.id == number).values(status='Y')
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def reject_visit(number):
        with Session() as sess:
            stmt = update(Visitors).where(Visitors.id == number).values(status='R')
            result = sess.execute(stmt)
            sess.commit()

        return result
