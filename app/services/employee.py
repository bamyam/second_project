from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.visitors import Employee
from app.dbfactory import Session


class EmployeeService:

    @staticmethod
    def get_all_employees():
        """
        데이터베이스에서 모든 직원 정보를 조회하여 반환합니다.

        Returns:
            List[Employee]: 조회된 직원 정보 목록
        """
        with Session() as session:
            statement = select(Employee)
            result = session.execute(statement).fetchall()
            return result