from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from secrets import user, password, host

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING. format(
    user=user, password=password, host=host, db="default")
)
Session = sessionmaker(bind=eng)
s = Session()

s.add_all(
    [
    Student(first_name="Adrian", last_name="Cristea"),
    Student(first_name="Andreea", last_name="Anca"),
    Student(first_name="Jessamine", last_name="Addison"),
    Student(first_name="Brena", last_name="Bugdale"),
    Student(first_name="Theobald", last_name="Oram"),
    Student(first_name="John", last_name="Smith")
    ]
)
s.commit()
