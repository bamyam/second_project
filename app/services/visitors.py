from app.models.visitors import Visitors
from sqlalchemy import insert, select, and_
from app.dbfactory import Session


class VisitorsService:

    @staticmethod
    def insert_visitor(vmdto):
        data = VisitorsService.visitor_convert(vmdto)

        with Session() as sess:
            stmt = insert(Visitors).values(data)
            sess.execute(stmt)
            sess.commit()

            result = sess.query(Visitors.id).filter_by(name=data['name']).scalar()

            return result


    @staticmethod
    def visitor_convert(vmdto):
        data = vmdto.model_dump()
        mb = Visitors(**data)
        data = {
            'name': mb.name,
            'company_name': mb.company_name,
            'email': mb.email,
            'department_name': mb.department_name,
            'job_position': mb.job_position,
            'phone_number': mb.phone_number,
            'employee_id': mb.employee_id,
            'purpose': mb.purpose,
            'location_id': mb.location_id,
            'status': mb.status,
            'regdate': mb.regdate,
            'visitdate': mb.visit_date
        }

        return data

    @staticmethod
    def search_visitor(name, phone_number):
        with Session() as sess:
            # name과 phone_number를 모두 만족하는 방문객 정보 조회
            stmt = select(Visitors).where(and_(Visitors.name == name, Visitors.phone_number == phone_number))
            result = sess.execute(stmt).fetchall()

        return result