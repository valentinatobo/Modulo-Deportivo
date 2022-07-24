import json
import cx_Oracle
from flask import Flask, render_template, request, redirect, request_started, url_for
from jinja2 import Environment, FileSystemLoader
import os
app = Flask(__name__)
# try:
#     connection=cx_Oracle.connect(
#         user='MODULODEP',
#         password='1234',
#         dsn='localhost:1521/XE',
#         encoding='UTF-8'
#     )
#     cursor=connection.cursor()
#     # cursor.execute("INSERT INTO ROL (IDROL, DESCROL) VALUES ('3', 'Pasante')")
#     # cursor.execute("UPDATE ROL SET DESCROL = 'Pasante' WHERE IDROL = 2")
#     # cursor.execute("UPDATE ROL SET DESCROL = 'Entrenador' WHERE IDROL = 3")
#     connection.commit()
#     cursor.execute("SELECT * FROM ROL")
#     rows=cursor.fetchall()
#     for row in rows:
#         print(row)
# except Exception as ex:
#     print(ex)
# finally:
#     connection.close()
#     print("Conexión Finalizada")


@app.route('/')
def init():
    return index()


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

@app.route('/select')
def select_ROL():
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}'
        )
        cur = connection.cursor()
        cur.execute("SELECT * FROM ROL")
        rows=cur.fetchall()
        col=""
        for row in rows:
            col+=str(row)
    except Exception as ex:
        print("Exeption")
        col=ex
    finally:
        connection.close()
        col+=" Conexión Finalizada"
    return col
#Consulta tabla
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

@app.route('/addPersonal')
def personal_form():
    return render_template('form.html')

@app.route('/addPersonal', methods={'POST'})
def insert_personal():
    if request.method=='POST':
        id=request.form['idPersonal']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        tPersonal=request.form['tipoPersonal']
        sede=request.form['sede']
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
    return render_template('editUser.html', contact=rows)

@app.route('/edit/<string:id>',  methods={'POST'})
def preubasUpdate(id):
    if request.method=='POST':
        id=request.form['idPersonal']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        tPersonal=request.form['tipoPersonal']
        sede=request.form['sede']
    try:
        cdtls = get_credentials()
        connection = cx_Oracle.connect(
            f'{cdtls["user"]}/{cdtls["psswrd"]}@{cdtls["host"]}:{cdtls["port"]}/{cdtls["db"]}'
        )
        cur = connection.cursor()
        cur.execute(f"""SELECT IDSEDE FROM SEDE WHERE NOMBRESEDE='{sede}'""")
        __sede=cur.fetchall()[0][0]
        cur.execute(f"""SELECT IDROL FROM ROL WHERE DESCROL='{tPersonal}'""")
        __tPersonal=cur.fetchall()[0][0]
        query=f"""UPDATE PERSONAL SET IDROLFK='{__tPersonal}', IDSEDEFK='{__sede}', NOMBREDOCENTE='{nombre}', APELLIDODOCENTE='{apellido}'
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


