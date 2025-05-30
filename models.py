from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Float, Date
from typing import List

class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    students: Mapped[List['Student']] = relationship(back_populates='group')

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))

    group: Mapped['Group'] = relationship(back_populates='students')
    grades: Mapped[List['Grade']] = relationship(back_populates='student')

class Teacher(Base):
    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)

    subjects: Mapped[List['Subject']] = relationship(back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'))

    teacher: Mapped['Teacher'] = relationship(back_populates='subjects')
    grades: Mapped[List['Grade']] = relationship(back_populates='subject')

class Grade(Base):
    __tablename__ = 'grades'

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'))
    grade: Mapped[float] = mapped_column(Float, nullable=False)
    date_recieved: Mapped[Date] = mapped_column(Date, nullable=False)

    subject: Mapped['Subject'] = relationship(back_populates='grades')
    student: Mapped['Student'] = relationship(back_populates='grades')
