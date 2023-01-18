
from dotenv import dotenv_values, load_dotenv
from flask import abort, session
from sqlalchemy import func
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import column_property
from werkzeug.security import check_password_hash, generate_password_hash


from app import db


load_dotenv()
config = dotenv_values(".env")
autoIncrement = True


class Tabla(db.Model):  # type: ignore
    __tablename__ = 'tabla'
    columna1 = db.Column(db.String(7), primary_key=True)
    columna2 = db.Column(db.Integer, nullable=True)
    columna3 = db.Column(db.Integer, db.ForeignKey('Profesores.ID_Profesor'), nullable=False)

    def __init__(self, columna1, columna2,columna3):
        self.columna1 = columna1        
        self.columna2 = columna2
        self.columna3 = columna3

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'columna1': self.columna1,
            'columna2': self.columna2,
            'columna3': self.columna3,
        }

def create_tables():
    db.create_all()