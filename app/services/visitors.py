from app.models.visitors import Visitors
from sqlalchemy import insert
from app.dbfactory import Session

class VisitorsService:

    @staticmethod
    def insert_visitor(vmdto):
        data = VisitorsService.visitor_convert(vmdto)

        with Session() as sess:
            stmt = insert(Visitors).values(data)
            result = sess.execute(stmt)
            sess.commit()

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
            'employee_name': mb.employee_name,
            'purpose': mb.purpose,
            'location': mb.location,
            'status': mb.status,
            'regdate': mb.regdate
        }

        return data