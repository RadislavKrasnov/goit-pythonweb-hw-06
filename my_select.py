from sqlalchemy import func, desc
from connection import session
from sqlalchemy.orm import Session
from models import Student, Grade, Subject, Teacher, Group

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1(session: Session):
    return session.query(
        Student.first_name,
        Student.last_name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade) \
    .group_by(Student.id) \
    .order_by(desc('avg_grade')) \
    .limit(5) \
    .all()

# Знайти студента із найвищим середнім балом з певного предмета.
def select_2(session: Session, subject_id: int):
    return session.query(
        Student.first_name,
        Student.last_name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade) \
     .filter(Grade.subject_id == subject_id) \
     .group_by(Student.id) \
     .order_by(desc('avg_grade')) \
     .first()

# Знайти середній бал у групах з певного предмета.
def select_3(session: Session, subject_id: int):
    return session.query(
        Group.name,
        func.avg(Grade.grade).label('avg_grade')
    ) \
    .join(Grade.subject) \
    .filter(Grade.subject_id == subject_id) \
    .group_by(Group.id) \
    .all()

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4(session: Session):
    return session.query(func.avg(Grade.grade)).scalar()

# Знайти які курси читає певний викладач.
def select_5(session: Session, teacher_id: int):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

# Знайти список студентів у певній групі.
def select_6(session: Session, group_id: int):
    return session.query(
        Student.first_name,
        Student.last_name
    ).filter(Student.group_id == group_id).all()

# Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(session: Session, group_id: int, subject_id: int):
    return session.query(
        Student.first_name,
        Student.last_name,
        Grade.grade
    ).join(Student.grades) \
    .filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(session: Session, teacher_id: int):
    return session.query(
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade.subject) \
    .filter(Subject.teacher_id == teacher_id).scalar()

# Знайти список курсів, які відвідує певний студент.
def select_9(session: Session, student_id: int):
    return session.query(Subject.name) \
    .join(Subject.grades) \
    .filter(Grade.student_id == student_id) \
    .group_by(Subject.id).all()

# Список курсів, які певному студенту читає певний викладач.
def select_10(session: Session, student_id: int, teacher_id: int):
    return session.query(
        Subject.name
    ).join(Subject.grades) \
    .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id) \
    .group_by(Subject.id) \
    .all()

# Середній бал, який певний викладач ставить певному студентові.
def select_11(session: Session, student_id: int, teacher_id: int):
    return session.query(func.avg(Grade.grade)) \
    .join(Grade.subject) \
    .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).scalar()

# Оцінки студентів у певній групі з певного предмета на останньому занятті.
def select_12(session: Session, group_id: int, subject_id: int):
    subquery = session.query(func.max(Grade.date_recieved)) \
    .join(Student) \
    .filter(Student.group_id == group_id, Grade.subject_id == subject_id) \
    .scalar()

    return session.query(
        Student.first_name,
        Student.last_name,
        Grade.grade,
        Grade.date_recieved
    ).join(Student.grades) \
    .filter(
        Grade.subject_id == subject_id,
        Student.group_id == group_id,
        Grade.date_recieved == subquery
    ) \
    .all()

print(select_1(session))
print(select_2(session, 1))
print(select_3(session, 1))
print(select_4(session))
print(select_5(session, 1))
print(select_6(session, 1))
print(select_7(session, 1, 1))
print(select_8(session, 1))
print(select_9(session, 1))
print(select_10(session, 1, 1))
print(select_11(session, 1, 1))
print(select_12(session, 3, 7))
