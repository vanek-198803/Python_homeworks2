import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = 'postgresql://postgres:Vanek@localhost:5432/QA9'
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    user_id = Column(Integer, primary_key=True)
    level = Column(String, nullable=False)
    education_form = Column(String, nullable=False)
    subject_id = Column(Integer, nullable=False)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_add_student(db_session):
    new_student = Student(level="Undergraduate",
                          education_form="Full-time",
                          subject_id=1)
    db_session.add(new_student)
    db_session.commit()

    assert new_student.user_id is not None
    assert (db_session.query(Student).filter_by(level="Undergraduate")
            .count() == 1)


def test_update_student(db_session):
    student = (db_session.query(Student).filter_by(level="Undergraduate")
               .first())
    student.level = "Graduate"
    db_session.commit()

    updated_student = (db_session.query(Student).filter_by
                       (user_id=student.user_id).first())
    assert updated_student.level == "Graduate"


def test_delete_student(db_session):
    student = (db_session.query(Student).filter_by(level="Graduate")
               .first())
    db_session.delete(student)
    db_session.commit()

    assert (db_session.query(Student).filter_by(level="Graduate")
            .count() == 0)
