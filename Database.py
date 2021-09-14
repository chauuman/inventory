import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('procesos.db')

c = conn.cursor()

c.execute("""CREATE TABLE transaccion (
    id integer,
    fecha integer,
    cantidad_vendido real
    total real
    )""")