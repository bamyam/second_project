from sqlalchemy import update

from app.dbfactory import Session
from app.models.visitors import Visitors

class AdminService:
    @staticmethod
    def accept_visit(number):
        with Session() as sess:
            stmt = update(Visitors).where(Visitors.id == number).values(status='Y')
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def reject_visit(data):
        number = data['number']
        with Session() as sess:
            stmt = update(Visitors).where(Visitors.id == number).values(status='R')
            result = sess.execute(stmt)
            sess.commit()

        return result
