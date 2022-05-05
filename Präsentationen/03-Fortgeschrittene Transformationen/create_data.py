import sqlite3
import json
import csv 
import os

if os.path.isfile("Diddly_Squat_Farm.db"):
    os.remove("Diddly_Squat_Farm.db")

# Datensatz
fields_for_insert = [(5, 'Barn Ground', 10), (6, 'Bank', 10), (7, 'Far Brossler', 20)]

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("Diddly_Squat_Farm.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Datenbanktabelle erzeugen
cursor.execute('''CREATE TABLE IF NOT EXISTS fields
              (field_id INTEGER PRIMARY KEY, field_name TEXT, area_in_sqm INTEGER)''')

# Insert data
cursor.executemany("INSERT INTO fields VALUES(?, ?, ?)", fields_for_insert)
connection.commit()

print('We have inserted', cursor.rowcount, 'fields to the table.')
for row in cursor.execute('SELECT * FROM fields'):
        print(row)

# Verbindung beenden
connection.close()

vegetablesFile = open('Vegetables.json', 'w')
vegetablesData = [
    {
        "crop":"zucchini",
        "field": 5,
        "week": 1,
        "water_consumption": 6,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 1,
        "water_consumption": 4,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 2,
        "water_consumption": 5,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 2,
        "water_consumption": 4,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 3,
        "water_consumption": 6,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 3,
        "water_consumption": 5,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 4,
        "water_consumption": 7,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 4,
        "water_consumption": 3,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 5,
        "water_consumption": 7,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 5
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 5,
        "water_consumption": 6,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 6,
        "water_consumption": 9,
        "revenue": {
            "net": 8,
            "tax": 2
        },
        "yield_per_sqm": 10
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 1,
        "water_consumption": 7,
        "revenue": {
            "net": 0,
            "tax": 0
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 7,
        "water_consumption": 10,
        "revenue": {
            "net": 16,
            "tax": 4
        },
        "yield_per_sqm": 25
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 7,
        "water_consumption": 8,
        "revenue": {
            "net": 32,
            "tax": 8
        },
        "yield_per_sqm": 160
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 8,
        "water_consumption": 13,
        "revenue": {
            "net": 40,
            "tax": 10
        },
        "yield_per_sqm": 25
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 8,
        "water_consumption": 8,
        "revenue": {
            "net": 50,
            "tax": 12
        },
        "yield_per_sqm": 240
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 9,
        "water_consumption": 12,
        "revenue": {
            "net": 40,
            "tax": 10
        },
        "yield_per_sqm": 25
    },
    {
        "crop":"radish",
        "field": 6,
        "week": 1,
        "water_consumption": None,
        "revenue": {
            "net": 50,
            "tax": 12
        },
        "yield_per_sqm": 0
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 10,
        "water_consumption": 5,
        "revenue": {
            "net": 40,
            "tax": 10
        },
        "yield_per_sqm": 25
    },
    {
        "crop":"zucchini",
        "field": 5,
        "week": 11,
        "water_consumption": None,
        "revenue": {
            "net": 40,
            "tax": 10
        },
        "yield_per_sqm": 0
    }
]

json.dump(vegetablesData, vegetablesFile)
vegetablesFile.close()


fruitsFile = open('Fruits.csv', 'w')
fruitsData = [
    {
        "crop":"strawberries",
        "field": 7,
        "week": 1,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 2,
        "water_consumption": 10,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 3,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 4,
        "water_consumption": 14,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 5,
        "water_consumption": 14,
        "revenue": 0,
        "yield_per_sqm": 5
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 6,
        "water_consumption": 18,
        "revenue": 30,
        "yield_per_sqm": 10
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 1,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 2,
        "water_consumption": 10,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 3,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 7,
        "water_consumption": 20,
        "revenue": 60,
        "yield_per_sqm": 25
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 8,
        "water_consumption": 26,
        "revenue": 150,
        "yield_per_sqm": 25
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 9,
        "water_consumption": 24,
        "revenue": 150,
        "yield_per_sqm": 25
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 10,
        "water_consumption": 10,
        "revenue": 100,
        "yield_per_sqm": 25
    },
    {
        "crop":"strawberries",
        "field": 7,
        "week": 11,
        "water_consumption": None,
        "revenue": 150,
        "yield_per_sqm": 0
    }
]

csvWriter = csv.DictWriter(fruitsFile, ['crop', 'field', 'week', 'water_consumption', 'revenue', 'yield_per_sqm'])
csvWriter.writeheader()
csvWriter.writerows(fruitsData)
fruitsFile.close()

cornFile = open('Corn.json', 'w')
cornData = [
    {
        "crop":"corn",
        "field": 8,
        "week": 1,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 2,
        "water_consumption": 10,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 3,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 4,
        "water_consumption": 14,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 5,
        "water_consumption": 14,
        "revenue": 0,
        "yield_per_sqm": 5
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 6,
        "water_consumption": 18,
        "revenue": 30,
        "yield_per_sqm": 10
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 1,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 2,
        "water_consumption": 10,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 3,
        "water_consumption": 12,
        "revenue": 0,
        "yield_per_sqm": 0
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 7,
        "water_consumption": 20,
        "revenue": 60,
        "yield_per_sqm": 25
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 8,
        "water_consumption": 26,
        "revenue": 150,
        "yield_per_sqm": 25
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 9,
        "water_consumption": 24,
        "revenue": 150,
        "yield_per_sqm": 25
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 10,
        "water_consumption": 10,
        "revenue": 100,
        "yield_per_sqm": 25
    },
    {
        "crop":"corn",
        "field": 8,
        "week": 11,
        "water_consumption": None,
        "revenue": 150,
        "yield_per_sqm": 0
    }
]

json.dump(cornData, cornFile)
cornFile.close()