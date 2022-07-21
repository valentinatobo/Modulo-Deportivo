import cx_Oracle

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

