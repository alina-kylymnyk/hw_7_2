from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Teacher, Subject, Grade

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/hw7db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def select_1():
    return session.query(Student).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()

def select_2(subject_id):
    return session.query(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()

def select_3(subject_id):
    return (
        session.query(Group.group_name, func.avg(Grade.grade))
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(teacher_id):
    return session.query(Subject.subject_name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_id):
    return (
        session.query(Student, Grade.grade)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
def select_8(teacher_id):
    return session.query(func.avg(Grade.grade)).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(student_id):
    return session.query(Subject.subject_name).join(Grade).filter(Grade.student_id == student_id).all()

def select_10(student_id, teacher_id):
    return session.query(Subject.subject_name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()

def print_results():
    # Перевірка результатів запитів
    print("Top 5 students by average grade:")
    results = select_1()
    for student in results:
        print(student.student_name)  # Correct attribute

    print("\nTop student for subject ID 1:")
    top_student = select_2(1)
    print(top_student.student_name)  # Correct attribute

    print("\nAverage grades for subject ID 1 by group:")
    avg_grades = select_3(1)
    for group_name, avg_grade in avg_grades:
        print(f"{group_name}: {avg_grade}")

    print("\nAverage grade for all students:")
    avg_grade = select_4()
    print(avg_grade)

    print("\nSubjects taught by teacher ID 1:")
    subjects = select_5(1)
    for subject in subjects:
        print(subject.subject_name)

    print("\nStudents in group ID 1:")
    students = select_6(1)
    for student in students:
        print(student.student_name)  # Correct attribute

    print("\nGrades for students in group ID 1 for subject ID 1:")
    grades = select_7(1, 1)
    for result in grades:
        print(f"Result type: {type(result)}")
        print(f"Result content: {result}")
        student, grade = result
        print(f"{student.student_name}: {grade}")  # Correct attribute

    print("\nAverage grade given by teacher ID 1:")
    avg_grade = select_8(1)
    print(avg_grade)

    print("\nSubjects attended by student ID 1:")
    subjects = select_9(1)
    for subject in subjects:
        print(subject.subject_name)

    print("\nSubjects taught by teacher ID 1 attended by student ID 1:")
    subjects = select_10(1, 1)
    for subject in subjects:
        print(subject.subject_name)

if __name__ == "__main__":
    print_results()
