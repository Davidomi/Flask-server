import secrets
from config import Config
from sqlalchemy import desc

from flask_mail import Mail, Message
from flask import Blueprint, request, session, redirect, url_for,flash, render_template, copy_current_request_context
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import threading
import json
from time import sleep
from app import mail

from .models import *
from datetime import datetime, time
from werkzeug.security import generate_password_hash, check_password_hash


file = open("./app/templates/json/form.json", "r")
json_form = json.load(file)




bp = Blueprint('main', __name__)
@bp.route('/')
def index():
    return render_template('login.html', index=True)

@bp.route('/cover')
def cover():
    curs=Cursos.query.all()
    print(curs)

    return render_template('cover.html', curs=curs)

@bp.route("/form")
def formu():
    
    file = open("./app/templates/json/form.json", "r")
    json_form = json.load(file)
    title = "Formularis"
    html = "<div class='content  div_flex_cards'>        <div class='row'>"
    #vamos a buscar todos los formularis que hay en el json
    for i in json_form:
        html+="""
        <div class="col ">
          <div class="card blue-grey darken-1 cards_form">
            <div class="card-content white-text">
              <span class="card-title">"""+i["title"]+"""</span>
            </div>
            <div class="card-action">
              <a href="/form/"""+i["form"]+""" ">Accedir</a>
            </div>
          </div>
        </div>
        """
    html+="</div></div>"

    
    
    return render_template("form.html", form=html, title=title)

   

@bp.route("/form/<string:form>", methods=["GET"])# type: ignore
def form(form):
    html = "<form class='regist-form' method='POST' action='/form/"+form+"/save'>"

    if form:
        for i in json_form:
            if i["form"] == form:
                title = i["title"]
                content = i["content"]
                
                for j in content:
                    html+='<div class="input-field col s6 m6 l6">'
                    
                    #vamos a crear inputs segun el tipo de input que sea
                    if content[j]["type"] == "select":
                        html+='<select name="'+content[j]["options"]["name"]+'" id="'+content[j]["options"]["id"]+'" class="'+content[j]["options"]["class"]+'">'
                        html+='<option value="" disabled selected>'+content[j]["options"]["name"]+'</option>'
                        #comprobamos si el select es de tipo json o string
                        if content[j]["options"]["select"]["type"] == "json":
                            for k in content[j]["options"]["select"]["value"]:
                                html+='<option value="'+content[j]["options"]["select"]["value"][k]+'">'+content[j]["options"]["select"]["value"][k]+'</option>'
                            
                        else:
                            #buscamos el nombre de la tabla en la que se encuentra el select
                            table = content[j]["options"]["select"]["value"]["table"]
                            info = content[j]["options"]["select"]["value"]["info"]
                            #convertimos el valor de table en una variable
                            value = eval(table).query.all()
                            print(value)
                            id=str(info["id"])
                            name=str(info["name"])
                            for k in value:
                                html+='<option value="'+str(k.__getattribute__(id))+'">'+str(k.__getattribute__(name))+'</option>'
                                
                        if content[j]["required"] == "1":
                        
                            html+=' required'
                        else :
                            html+=''
                            
                        html+='</select>'
                    else:
                        html+='<label for="'+content[j]["label"]["for"]+'" class="'+content[j]["label"]["class"]+' ">'+content[j]["label"]["name"]+'</label> '                   
                        if content[j]["type"] == "text" or content[j]["type"] == "email" or content[j]["type"] == "password" or content[j]["type"] == "date" or content[j]["type"] == "number":
                            html+='<input type="'+content[j]["type"]+'" name="'+content[j]["options"]["name"]+'" id="'+content[j]["options"]["id"]+'" class="'+content[j]["options"]["class"]+'"'
                            if content[j]["required"] == "1":
                            
                                html+=' required'
                            else :
                                html+=''
                            html+='/>'
                        elif content[j]["type"] == "file":
                            html+='<input type="'+content[j]["type"]+'" name="'+content[j]["options"]["name"]+'" id="'+content[j]["options"]["id"]+'" class="'+content[j]["options"]["class"]+'"'
                            if content[j]["required"] == "1":
                            
                                html+=' required'
                            else :
                                html+=''
                            
                            html+='/>'
                    
                    
                    
                    html+='</div>'
        html+="""<button
            class="btn waves-effect waves-light col s12"
            type="submit"
            name="action"
            ng-click="guardar()"
          >
            Guardar
          </button> </form>"""
    else :
        html = "No se ha encontrado el formulario"
    
                        
    return render_template("form.html", form=html, title=title)# type: ignore

#Guardar formularis
@bp.route("/form/<string:form>/save", methods=["POST"])# type: ignore
def save_formu(form):
    data = request.form
    if form:
        for i in json_form:
            if i["form"] == form:
                print(data)
                #cogemos la base de datos donde debemos guardar la informacion
                database = eval(i["database"])
                print(dir(database))
                for x in i["content"]:
                    setattr(database, x, data[x])
                database.save()

                    
                    
                print(database)
    if form == "cursos" and 1 == 0 :
        curs = Cursos(
            Nom=request.form["Nom"],
            Abreb=request.form["Abreb"],
            Durada=request.form["Durada"],
            Data_fi=request.form["Data_fi"],
            Data_inici=request.form["Data_inici"],
            Curs=request.form["Curs"],
            Tutor=request.form["Tutor"],
            Horario=request.form["Horario"])
        curs.save()
    
    # return redirect(url_for("main.formu"))
    return("ok")






@bp.route('/registr_alumnes')
def registr_alumnes():
    return render_template('registr_alumnes.html')