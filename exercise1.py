from sqlalchemy.orm import sessionmaker
from secrets import host, user, password
from models import Student, Base, Locker, Adress
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
        Adress(student=1, street_name="Republicii", number=3, city="Turda"),
        Adress(student=2, street_name="Cheii", number=34, city="Sighisoara"),
        Adress(student=3, street_name="Dorobantilor", number=45, city="Cluj-Napoca"),
        Adress(student=4, street_name="Potaisa", number=54, city="CAmpia-Turzii"),
        Adress(student=5, street_name="Sandulesti",number=5, city="Sibiu"),
        Adress(student=6, street_name="Ana-Ipatescu", number=23, city="Bucuresti")
        ])
    s.commit()
except IntegrityError:
    s.rollback()
    print("Adress was already created")
rows = s.query(Adress, Student).join(Student).filter(Adress.number == 3)
for row in rows:
    adress, students = row
    print(f"Student's adress is {adress.student}")













