from datetime import datetime 
from flask_sqlalchemy import SQLALchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLALchemy()


class Base(db.Models):

    __abstract__ = True

    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
            db.DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow
            )

user_job = db.Table(
        'user_job',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),        db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))        
        )

class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    resume = de.relationship('Resume', uselist=False)
    collect_jobs = db.relationship('job', secondary=user_job)
    upload_resume_url = db.Column(db.String(64))

    def __repr__(self):
        return '<User:{}>'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role = self.ROLE_ADMIN
    @property
    def is_company(self):
        return self.role = self.ROLE_COMPANY

class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeginKey('user.id'))
    user = db.relationship('User', uselist=Flase)
    job_experiences = db.relationship('JobExperience')
    edu_experiences = db.relationship('EduExperience')
    project_experiences = db.relationship('ProjectExperience')

    def profile(self):
        pass 


class Experience(Base):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    begin_at = db.Column(db.DateTime)
    end_at = db.Column(db.DateTime)

    description = db.Column(db.String(1024))


class EduExperience(Experience):

    school = db.Column(db.String(32),nullable=False)
    specialty = db.Column(db.String(32),nullable=False)
    degree = db.Column(db.String(16))
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))
    resume = db.relationship('Resume', uselist=False)


class ProjectExperice(Experience):

    name = db.Column(db.String(32),nullable=False)
    role = db.Column(db.String(32))
    technologys = db.Column(db.String(64))
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))
    resume = db.relationship('Resume', uselist=False)



