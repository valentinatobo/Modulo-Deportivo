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
#     print(connection.version)
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
#     print("Exeption")
#     print(ex)
# finally:
#     connection.close()
#     print("Conexión Finalizada")


@app.route('/')
def init():
    print("coneccion index")
    return index()


# path for index
@app.route('/index')
def index():
    titulo = "Modulo Deportivo UD"
    print("redireccionado")
    return render_template('formulario.html', titulo=titulo)


# Prueba de Conexion a la Base de Datos
@app.route('/con')
def insert_default():
    try:
        cdtls = get_credentials()
        print(f"Credentials: {cdtls}")
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
def select_def():
    try:
        cdtls = get_credentials()
        print(f"Credentials: {cdtls}")
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

def get_credentials():
    # Opening JSON file
    f = open('credenciales.json')
    # returns JSON object as a dictionary
    db = json.load(f)
    f.close
    return db

if __name__ == "__main__":
    app.run(debug=True)


