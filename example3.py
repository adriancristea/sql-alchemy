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

rows = s.query(Student) .all()
for row in rows:
    print(row)

print("---")
total = s.query(Student).count()
print(f"Total: {total}")

print("---")
query_result = s.query(Student).filter(Student.id >= 2, Student.first_name.like("Bre%"))
print("Found students:")
for row in query_result:
    print(row)
# Set new last name
andreeea = s.query(Student).filter(Student.first_name == "Andreea").first()
andreeea.last_name = "Cristea"
s.commit()

# Update multiple Students
brena = s.query(Student).filter(Student.first_name == "Brena")
for brena in brena:
    brena.last_name = "Dark"

s.commit()
