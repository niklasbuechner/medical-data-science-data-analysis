import petl as etl
import sqlite3


#Verbindug aufbauen
connection = sqlite3.connect('firma.db')

table = etl.fromdb(connection, 'SELECT * FROM personen')

print(table)