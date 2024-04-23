from app.models.visitors import Visitors
from sqlalchemy import insert
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