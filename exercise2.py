from sqlalchemy.orm import sessionmaker
from secrets import host, user, password
from models import Student, Base, Locker, Adress, Grades
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, InvalidRequestError


CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"


eng = create_engine(
    CONNECTION_STRING. format(
    user=user, password=password, host=host, db="default")
)

Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)
s = Session()

try:
    s.add_all([
        Grades(student=1, grade=6),
        Grades(student=2, grade=7),
        Grades(student=3, grade=8),
        Grades(student=4, grade=4),
        Grades(student=5, grade=6),
        Grades(student=6, grade=2)
    ])
    s.commit()
except IntegrityError:
    s.rollback()
    print("Grades was already created")
rows = s.query(Grades, Student).join(Grades).filter(Grades.number == 3)

