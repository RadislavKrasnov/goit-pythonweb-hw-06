import random
from connection import session
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Teacher, Subject, Grade

fake = Faker()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)

teachers = [
    Teacher(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(5)
]
session.add_all(teachers)

subjects = [
    Subject(name=fake.word().capitalize(), teacher=random.choice(teachers))
    for _ in range(8)
]
session.add_all(subjects)

students = [
    Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        group=random.choice(groups),
    )
    for _ in range(50)
]
session.add_all(students)

for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.randint(60, 100),
                date_recieved=fake.date_between(start_date="-1y", end_date="today"),
            )
            session.add(grade)

session.commit()
session.close()
