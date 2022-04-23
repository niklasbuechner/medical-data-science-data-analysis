
import os
import sqlite3
import sys
# Datensatz
fields_for_insert = [(1, 'Barn Ground'), (2, 'Bank'), (3, 'Far Brossler'), (4, 'Picket Piece'), (5, 'Buryhill North'), (6, 'Buryhill South'),(7, 'Washpool'), (8, 'Pea Furlong'), (9, 'Quarry'), (10, 'Road Field'), (11, 'Lower Washpool'), (12, 'Louse'), (13, 'Curdle Hill')]


# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("Diddly_Squat_Farm.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Datenbanktabelle erzeugen
cursor.execute('''CREATE TABLE IF NOT EXISTS Fields
              (field_ID INTEGER PRIMARY KEY, field_Name TEXT)''')

# Insert a row of data
#cursor.execute("INSERT INTO Fields VALUES(?,?)", fields_for_insert)

connection.commit()

cursor.executemany("INSERT INTO fields VALUES(?,?)", fields_for_insert)
print('We have inserted', cursor.rowcount, 'Fields to the table.')
for row in cursor.execute('SELECT * FROM Fields'):
        print(row)


# Verbindung beenden
connection.close()


