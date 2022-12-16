import sqlite3

conn=sqlite3.connect("baseDeDatos.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(50) NOT NULL,email VARCHAR(50) UNIQUE NOT NULL, nombreBDD VARCHAR(50) NOT NULL, apellidoBDD VARCHAR(50) NOT NULL, dniBDD VARCHAR(50) NOT NULL, nacimiento VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)")

def saveData(username,email,nombreBDD,apellidoBDD,dniBDD,nacimiento,password):
    cursor.execute("INSERT INTO usuarios VALUES (NULL,?,?,?,?,?,?,?)",(username,email,nombreBDD,apellidoBDD,dniBDD,nacimiento,password))
    conn.commit()

def loginUser(username,password):
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?",(username,password))
    if cursor.fetchone() is not None:
        return True
    else:
        return False
