import cx_Oracle
from flask import Flask,render_template, request, redirect, url_for
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

<<<<<<< HEAD
@app.route('/')
def Index():
    return "Hello World"
if __name__== "__main__":
    app.run(debug=True)
=======
try:
    connection=cx_Oracle.connect(
        user='MODULODEP',
        password='1234',
        dsn='localhost:1521/XE',
        encoding='UTF-8'
    )
    print(connection.version)
    cursor=connection.cursor()
    cursor.execute("INSERT INTO ROL (IDROL, DESCROL) VALUES ('1', 'Entrenador')")
    # cursor.execute("UPDATE ROL SET DESCROL = 'Pasante' WHERE IDROL = 2")
    # cursor.execute("UPDATE ROL SET DESCROL = 'Entrenador' WHERE IDROL = 1")
    connection.commit()
    cursor.execute("SELECT * FROM ROL")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Exeption")
    print(ex)
finally:
    connection.close()
    print("Conexión Finalizada")
>>>>>>> 013a2419d272e3ff652c6263e41728493b56f415

@app.route('/addPersonal', methods={'POST'})
def addPersonal():
    if request.method=="POST":
        1+1
