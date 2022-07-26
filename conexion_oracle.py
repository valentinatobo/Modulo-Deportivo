import json
import cx_Oracle
from flask import Flask, render_template, request, redirect, request_started, url_for
from jinja2 import Environment, FileSystemLoader
import os
app = Flask(__name__)

#obtiene los roles y sedes
def getInfoSelec():
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}')
        cur = connection.cursor()
        cur.execute("SELECT * FROM ROL")
        rols=cur.fetchall()
        cur.execute("SELECT * FROM SEDE")
        sedes=cur.fetchall()
    except Exception as ex:
        print("Exeption")
        return str(ex)
    finally:
        connection.close()
    return rols, sedes

#obtiene el rol y la sede del id
def getInfo(id):
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}')
        cur = connection.cursor()
        cur.execute(f"""SELECT P.IDROLFK, R.DESCROL
                        FROM PERSONAL P, ROL R
                        WHERE '{id}'=P.IDPERSONAL AND P.IDROLFK=R.IDROL""")
        infoRol=cur.fetchall()
        cur.execute(f"""SELECT P.IDSEDEFK, S.NOMBRESEDE
                        FROM PERSONAL P, SEDE S
                        WHERE '{id}'=P.IDPERSONAL AND P.IDSEDEFK=S.IDSEDE""")
        infoSede=cur.fetchall()
        
    except Exception as ex:
        print("Exeption metodo get")
        return str(ex)
    finally:
        connection.close()
    return infoRol[0], infoSede[0]

@app.route('/')
def init():
    return get_personal()


# path for index
@app.route('/index')
def index():
    titulo = "Prueba"
    return get_personal()


# Prueba de Conexion a la Base de Datos
@app.route('/con')
def insert_default():
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}'
        )
        cur = connection.cursor()
        #   Prueba de Conexion
        cur.execute("SELECT * FROM ROL")
        col = cur.fetchone()[0]
        cur.close()
    except Exception as ex:
        print("Exeption")
        col=ex
    finally:
        connection.close()
        col+="Conexión Finalizada"
    return col

#Consulta informacion personal
@app.route('/Personal')
def get_personal():
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}'
        )
        cur = connection.cursor()
        cur.execute("""SELECT P.IDPERSONAL, R.DESCROL, S.NOMBRESEDE, P.NOMBREDOCENTE, P.APELLIDODOCENTE
                        FROM PERSONAL P, ROL R, SEDE S
                        WHERE P.IDROLFK=R.IDROL AND P.IDSEDEFK=S.IDSEDE""")
        rows=cur.fetchall()
    except Exception as ex:
        print("Exeption")
        return str(ex)
    finally:
        connection.close()
    return render_template('tabla.html', contacts=rows)

#Agrega sedes y roles al form
@app.route('/addPersonal')
def personal_form():
    info = getInfoSelec();
    return render_template('form.html', infoRols = info[0], infoSedes = info[1])

#Crear nuevo personal
@app.route('/addPersonal', methods={'POST'})
def insert_personal():
    if request.method=='POST':
        id=request.form['idPersonal']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        tPersonal=request.form['tPersonal']
        sede=request.form['tsede']
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}')
        cur = connection.cursor()
        query=f"""INSERT INTO PERSONAL (IDPERSONAL, IDROLFK, IDSEDEFK, NOMBREDOCENTE, APELLIDODOCENTE)
                        VALUES ('{id}','{tPersonal}','{sede}','{nombre}','{apellido}')"""
        cur.execute(query)
        connection.commit()
    except Exception as ex:
        print("Exeption")
        return str(ex)
    finally:
        connection.close()
    return get_personal()

#obtener la información del usuario segun su id
@app.route('/edit/<string:id>')
def edit_form(id):
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}'
        )
        cur = connection.cursor()
        cur.execute(f"""SELECT P.IDPERSONAL, R.DESCROL, S.NOMBRESEDE, P.NOMBREDOCENTE, P.APELLIDODOCENTE
                        FROM PERSONAL P, ROL R, SEDE S
                        WHERE P.IDROLFK=R.IDROL AND P.IDSEDEFK=S.IDSEDE AND '{id}'=P.IDPERSONAL""")
        rows=cur.fetchall()[0]
    except Exception as ex:
        print("Exeption")
        return str(ex)
    finally:
        connection.close()
    info = getInfoSelec();
    get_Info =  getInfo(id);
    return render_template('editUser.html', contact=rows,infoRols = info[0], infoSedes = info[1], infoSelec = get_Info)

#editar la información del usuario en la bd
@app.route('/edit/<string:id>',  methods={'POST'})
def preubasUpdate(id):
    if request.method=='POST':
        id=request.form['idPersonal']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        Personal=request.form['tPersonal']
        tsede=request.form['tsede']
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}'
        )
        cur = connection.cursor()
        query=f"""UPDATE PERSONAL SET IDROLFK='{Personal}', IDSEDEFK='{tsede}', NOMBREDOCENTE='{nombre}', APELLIDODOCENTE='{apellido}'
                        WHERE  IDPERSONAL='{id}'"""
        cur.execute(query)
        connection.commit()
    except Exception as ex:
        print("Exeption")
        return str(ex)
    finally:
        connection.close()
    return get_personal()

def get_credentials():
    # Opening JSON file
    f = open('credenciales.json')
    # returns JSON object as a dictionary
    db = json.load(f)
    f.close
    return db

if __name__ == "__main__":
    app.run(debug=True)


