from . import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')


""" 
class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1))

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    follow_up_number = db.Column(db.Integer)

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    group = db.Column(db.String(255))
    image_index = db.Column(db.String(255))
    patient_age = db.Column(db.Integer)
    view_position = db.Column(db.String(255))
    original_image_width_height = db.Column(db.String(255))
    original_image_pixel_spacing = db.Column(db.String(255))

class Finding(db.Model):
    __tablename__ = 'findings'
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    finding_label = db.Column(db.String(255))
 """

""" 
CREATE TABLE Patients (
PatientID INT PRIMARY KEY,
PatientGender CHAR(1)
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    PatientID INT,
    FollowUpNumber INT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

CREATE TABLE Images (
    ImageID INT PRIMARY KEY,
    AppointmentID INT,
    Group VARCHAR(255),
    ImageIndex VARCHAR(255),
    PatientAge INT,
    ViewPosition VARCHAR(255),
    OriginalImageWidthHeight VARCHAR(255),
    OriginalImagePixelSpacing VARCHAR(255),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

CREATE TABLE Findings (
    FindingID INT PRIMARY KEY,
    ImageID INT,
    FindingLabel VARCHAR(255),
    FOREIGN KEY (ImageID) REFERENCES Images(ImageID)
); 
"""
