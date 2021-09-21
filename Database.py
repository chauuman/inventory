import sqlite3 
import os 
os.system("cls")


miConexion = sqlite3.connect("BDinventory.db") 
print("Conectado Satisfactoriamente")
miCursor = miConexion.cursor() # miCursor.execute("CREATE TABLE Cursos (idCurso INTEGER NOT NULL UNIQUE, NombreCurso TEXT NOT NULL, PRIMARY KEY(idCurso AUTOINCREMENT))")
miCursor.execute("INSERT INTO IyE_negocio (Id) VALUES ('1011')")

miCursor.close()
miConexion.close()
