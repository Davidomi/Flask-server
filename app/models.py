
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


class Cursos(db.Model):  # type: ignore
    __tablename__ = 'Cursos'
    Abreb = db.Column(db.String(7), primary_key=True)
    Nom = db.Column(db.String(50), primary_key=True)
    Durada = db.Column(db.Integer, nullable=True)
    Data_inici = db.Column(db.DateTime, nullable=False)
    Data_fi = db.Column(db.DateTime, nullable=False)
    Curs = db.Column(db.Integer, nullable=False)
    Horario = db.Column(db.Integer, nullable=False) 
    Tutor = db.Column(db.Integer, db.ForeignKey('Profesores.ID_Profesor'), nullable=False)

    def __init__(self, Abreb, Nom, Durada,Data_inici,Data_fi, Curs,Horario,Tutor):
        self.Abreb = Abreb
        self.Nom = Nom
        self.Durada = Durada
        self.Data_inici = Data_inici
        self.Data_fi = Data_fi
        self.Curs = Curs
        self.Horario = Horario
        self.Tutor = Tutor

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'Abreb': self.Abreb,
            'Nom': self.Nom,
            'Durada': self.Durada,
            'Data_inici': self.Data_inici,
            'Data_fi': self.Data_fi,
            'Curs': self.Curs,
            'Horario': self.Horario,
            'Tutor': self.Tutor,
        }


#Creamos la tabla de los modulos, la cual contiene el nombre, el ID_Curso, Fin e inicio, Profesor/Profesores que lo dan
class Modulos(db.Model): # type: ignore
    ID_Modulo = db.Column(db.Integer, primary_key=True)
    ID_Curso = db.Column(db.String(7), db.ForeignKey('Cursos.Abreb'), nullable=False)
    Nom = db.Column(db.String(30), nullable=False)
    Inicio = db.Column(db.DateTime, nullable=False)
    Fin = db.Column(db.DateTime, nullable=False)
    Professor = db.Column(db.Integer, db.ForeignKey('Profesores.ID_Profesor'), nullable=False)

    def __init__(self,ID_Modulo, ID_Curso, Nom, Inicio, Fin, Professor) :
        self.ID_Modulo = ID_Modulo
        self.ID_Curso = ID_Curso
        self.Nom = Nom
        self.Inicio = Inicio
        self.Fin = Fin
        self.Professor = Professor
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def serialize(self):
        return {
            'ID_Modulo': self.ID_Modulo,
            'ID_Curso': self.ID_Curso,
            'Nom': self.Nom,
            'Inicio': self.Inicio,
            'Fin': self.Fin, 
            'Professor': self.Professor,
        }

#Creacion de la tabla UFs, donde vamos ha guardar la informacion(Nombre_Modulos,ID_UF, Nombre,ID_Curso,Nombre_Uf,Id_Profesor, Horas, Inicio,Fin )
class UFs(db.Model):  # type: ignore
    ID_UF = db.Column(db.Integer, primary_key=True)
    ID_Modulo = db.Column(db.Integer, db.ForeignKey('Modulos.ID_Modulo'), nullable=False)
    ID_Curso = db.Column(db.String(7), db.ForeignKey('Cursos.Abreb'), nullable=False)
    Nom = db.Column(db.String(30), nullable=False)
    Hora = db.Column(db.Integer, nullable=False)
    Inicio = db.Column(db.DateTime, nullable=False)
    Fin = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, ID_UF, ID_Modulo, ID_Curso, Nom, Hora, Inicio, Fin) :
        self.ID_UF = ID_UF
        self.ID_Modulo = ID_Modulo
        self.ID_Curso = ID_Curso
        self.Nom = Nom
        self.Hora = Hora
        self.Inicio = Inicio
        self.Fin = Fin
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def serialize(self):
        return {
            'ID_UF': self.ID_UF,
            'ID_Modulo': self.ID_Modulo,
            'ID_Curso': self.ID_Curso,
            'Nom': self.Nom,
            'Hora': self.Hora,
            'Inicio': self.Inicio,
            'Fin': self.Fin,
        }
    
#Creacion de la tabla de los alumnos, donde vamos a guardar la informacion de los alumnos(DNIque sera la primarykey,Nombre,Apellidos,Matricula,Email,Id_Curso,Fecha_Nacimiento, Genero,Foto,Numero de la tarjeta sanitario, municipio, probvincia, Pais )
class Alumnos(db.Model):  # type: ignore
    __tablename__ = 'Alumnos'
    DNI = db.Column(db.String(9), primary_key=True)
    Nom = db.Column(db.String(30), nullable=False)
    Apellidos = db.Column(db.String(30), nullable=False)
    Matricula = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    ID_Curso = db.Column(db.String(7), db.ForeignKey('Cursos.Abreb'), nullable=False)
    Fecha_Nacimiento = db.Column(db.DateTime, nullable=False)
    Genero = db.Column(db.String(30), nullable=False)
    Foto = db.Column(db.String(30), nullable=False)
    Tarjeta_Sanitaria = db.Column(db.String(30), nullable=False)
    Municipio = db.Column(db.String(30), nullable=False)
    Provincia = db.Column(db.String(30), nullable=False)
    Pais = db.Column(db.String(30), nullable=False)

    def __init__(self, DNI, Nom, Apellidos, Matricula, Email, ID_Curso, Fecha_Nacimiento, Genero, Foto, Tarjeta_Sanitaria, Municipio, Provincia, Pais) :
        self.DNI = DNI
        self.Nom = Nom
        self.Apellidos = Apellidos
        self.Matricula = Matricula
        self.Email = Email
        self.ID_Curso = ID_Curso
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Genero = Genero
        self.Foto = Foto
        self.Tarjeta_Sanitaria = Tarjeta_Sanitaria
        self.Municipio = Municipio
        self.Provincia = Provincia
        self.Pais = Pais
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def serialize(self):
        return {
            'DNI': self.DNI,
            'Nom': self.Nom,
            'Apellidos': self.Apellidos,
            'Matricula': self.Matricula,
            'Email': self.Email,
            'ID_Curso': self.ID_Curso,
            'Fecha_Nacimiento': self.Fecha_Nacimiento,
            'Genero': self.Genero,
            'Foto': self.Foto,
            'Tarjeta_Sanitaria': self.Tarjeta_Sanitaria,
            'Municipio': self.Municipio,
            'Provincia': self.Provincia,
            'Pais': self.Pais,
        }
#Creamos la tabla  de los Profesores, la cual contendra (ID_Profesor(PRimary key), nombre, apellidos, mail, data_Naix, Genero,Foto, Nacionalidd,Municipio,Provincia,Pais, Data_naix, Telefono )
class Profesores(db.Model):  # type: ignore
    __tablename__ = 'Profesores'
    ID_Profesor = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(30), nullable=False)
    Apellidos = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    Fecha_Nacimiento = db.Column(db.DateTime, nullable=False)
    Genero = db.Column(db.String(30), nullable=False)
    Foto = db.Column(db.String(30), nullable=False)
    Nacionalidad = db.Column(db.String(30), nullable=False)
    Municipio = db.Column(db.String(30), nullable=False)
    Provincia = db.Column(db.String(30), nullable=False)
    Pais = db.Column(db.String(30), nullable=False)
    Telefono = db.Column(db.String(30), nullable=False)
    
    def __init__(self, ID_Profesor, Nom, Apellidos, Email, Fecha_Nacimiento, Genero, Foto, Nacionalidad, Municipio, Provincia, Pais, Telefono) :
        self.ID_Profesor = ID_Profesor
        self.Nom = Nom
        self.Apellidos = Apellidos
        self.Email = Email
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Genero = Genero
        self.Foto = Foto
        self.Nacionalidad = Nacionalidad
        self.Municipio = Municipio
        self.Provincia = Provincia
        self.Pais = Pais
        self.Telefono = Telefono
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        
    def serialize(self):
        return {
            'ID_Profesor': self.ID_Profesor,
            'Nom': self.Nom,
            'Apellidos': self.Apellidos,
            'Email': self.Email,
            'Fecha_Nacimiento': self.Fecha_Nacimiento,
            'Genero': self.Genero,
            'Foto': self.Foto,
            'Nacionalidad': self.Nacionalidad,
            'Municipio': self.Municipio,
            'Provincia': self.Provincia,
            'Pais': self.Pais,
            'Telefono': self.Telefono,
        }

#Creamos la tabla de los profesores que imparten las UFs, la cual contendra (ID_UF, ID_Profesor)
class Profesores_UFs(db.Model):  # type: ignore
    __tablename__ = 'Profesores_UFs'
    ID_UF = db.Column(db.Integer, db.ForeignKey('UFs.ID_UF'), nullable=False, primary_key=True)
    ID_Profesor = db.Column(db.Integer, db.ForeignKey('Profesores.ID_Profesor'), nullable=False , primary_key=True)

#Creamos la tabla de los alumnos que estan matriculados en un curso, la cual contendra (DNI, ID_Curso)
class Alumnos_Cursos(db.Model):  # type: ignore
    __tablename__ = 'Alumnos_Cursos'
    DNI = db.Column(db.String(9), db.ForeignKey('Alumnos.DNI'), nullable=False, primary_key=True)
    ID_Curso = db.Column(db.String(7), db.ForeignKey('Cursos.Abreb'), nullable=False, primary_key=True)

#Creamos la tabla de los alumnos que estan matriculados en un modulo, la cual contendra (DNI, ID_Modulo)
class Alumnos_Modulos(db.Model):  # type: ignore
    __tablename__ = 'Alumnos_Modulos'
    DNI = db.Column(db.String(9), db.ForeignKey('Alumnos.DNI'), nullable=False, primary_key=True)
    ID_Modulo = db.Column(db.Integer, db.ForeignKey('Modulos.ID_Modulo'), nullable=False, primary_key=True)

#Creamos la tabla de los alumnos que estan matriculados en una UF, la cual contendra (DNI, ID_UF)
class Alumnos_UFs(db.Model):  # type: ignore
    __tablename__ = 'Alumnos_UFs'
    DNI = db.Column(db.String(9), db.ForeignKey('Alumnos.DNI'), nullable=False, primary_key=True)
    ID_UF = db.Column(db.Integer, db.ForeignKey('UFs.ID_UF'), nullable=False, primary_key=True)


#Creamos la tabla de los padres para los alumnos menores de edad(DNI(Primarykey), Nombre, apellidos,mail,Fecha necimiento, genero, foto, nacionalidad, municipio, provincia, pais , frcha nacimiento, telefono)

class Padres(db.Model):  # type: ignore
    __tablename__ = 'Padres'
    DNI = db.Column(db.String(9), primary_key=True)
    Nom = db.Column(db.String(30), nullable=False)
    Apellidos = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    Fecha_Nacimiento = db.Column(db.DateTime, nullable=False)
    Genero = db.Column(db.String(30), nullable=False)
    Foto = db.Column(db.String(30), nullable=False)
    Nacionalidad = db.Column(db.String(30), nullable=False)
    Municipio = db.Column(db.String(30), nullable=False)
    Provincia = db.Column(db.String(30), nullable=False)
    Pais = db.Column(db.String(30), nullable=False)
    Telefono = db.Column(db.String(30), nullable=False)


#Creamos la tabla de los padres de los alumnos menores de edad, la cual contendra (DNI, DNI_Padre)
class Padres_Alumnos(db.Model):  # type: ignore
    __tablename__ = 'Padres_Alumnos'
    DNI_Alumno = db.Column(db.String(9), db.ForeignKey('Alumnos.DNI'), nullable=False, primary_key=True)
    DNI_Padre = db.Column(db.String(9), db.ForeignKey('Padres.DNI'), nullable=False, primary_key=True)


#Creamos la tabla de las notas , la cual contendra (ID_UF,,Nota, DNI_Alumno, y si la nota se ha puesto Hordinaria o no)
class Notas(db.Model):  # type: ignore
    __tablename__ = 'Notas'
    ID_UF = db.Column(db.Integer, db.ForeignKey('UFs.ID_UF'), nullable=False)
    Nota = db.Column(db.Integer, nullable=False)
    DNI_Alumno = db.Column(db.String(9), db.ForeignKey('Alumnos.DNI'), nullable=False)
    Hordinaria = db.Column(db.Boolean, nullable=False)
    ID_Nota = db.Column(db.Integer, primary_key=True, autoincrement=True)


#Creamos la tabla para los logins, la cual contiene el Id_professor, passwrd, el rol, la ultima conexion, y la ultima vexz que se cambio la contrase;a
class Logins(db.Model):  # type: ignore
    __tablename__ = 'Logins'
    ID_Profesor = db.Column(db.Integer, db.ForeignKey('Profesores.ID_Profesor'), nullable=False, primary_key=True)
    Passwrd = db.Column(db.String(255), nullable=False)
    Rol = db.Column(db.String(30), nullable=False)
    Ultima_Conexion = db.Column(db.DateTime, nullable=False)
    Ultima_Cambio_Contraseña = db.Column(db.DateTime, nullable=False)


def create_tables():
    db.create_all()