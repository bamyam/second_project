from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import config
from app.models import employee, location, visitors

engine = create_engine(config.db_conn, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def db_startup():
    employee.Base.metadata.create_all(engine)
    location.Base.metadata.create_all(engine)
    visitors.Base.metadata.create_all(engine)