import sqlite3
connection = sqlite3.connect("client.sqlite")
cursor = connection.cursor()
facility_list = ("Сварочный аппарат №1", "Пильный аппарат №2", "Фрезер №3")
for facility in facility_list:
    cursor.execute(f'''INSERT INTO endpoints (name, active)
                    VALUES ("{facility}", "true")''')
connection.commit()
