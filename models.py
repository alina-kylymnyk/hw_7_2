from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, index=True)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, index=True)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date_of = Column(Date)
    student = relationship('Student')
    subject = relationship('Subject')
