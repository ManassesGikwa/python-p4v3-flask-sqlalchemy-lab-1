from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

#SQLAlchemy instance
db = SQLAlchemy()

# Earthquake model
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

# Student model
class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    course = db.relationship('Course', back_populates="students")

# Course model
class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String)

    students = db.relationship('Student', back_populates="course")
