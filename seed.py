from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
from faker import Faker
import random
from datetime import datetime

# Налаштування бази даних
DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/hw7db"

# Створення engine і session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Ініціалізація Faker
fake = Faker()

def fill_db():
    # Очищення існуючих даних
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Створення груп
    groups = []
    for _ in range(3):
        group = Group(group_name=fake.word())
        session.add(group)
        groups.append(group)
    session.commit()

    # Створення викладачів
    teachers = []
    for _ in range(5):
        teacher = Teacher(teacher_name=fake.name())
        session.add(teacher)
        teachers.append(teacher)
    session.commit()

    # Створення предметів
    subjects = []
    for _ in range(8):
        subject = Subject(subject_name=fake.word(), teacher_id=random.choice(teachers).id)
        session.add(subject)
        subjects.append(subject)
    session.commit()

    # Створення студентів
    students = []
    for _ in range(50):
        student = Student(student_name=fake.name(), group_id=random.choice(groups).id)
        session.add(student)
        students.append(student)
    session.commit()

    # Створення оцінок
    for student in students:
        for _ in range(random.randint(1, 20)):  # До 20 оцінок для кожного студента
            grade = Grade(
                student_id=student.id,
                subject_id=random.choice(subjects).id,
                grade=random.randint(1, 5),
                date_of=fake.date_this_decade()
            )
            session.add(grade)
    session.commit()

if __name__ == "__main__":
    fill_db()
