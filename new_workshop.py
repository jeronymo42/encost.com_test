import sqlite3
connection = sqlite3.connect("client.sqlite")
cursor = connection.cursor()
facility_list = ("Сварочный аппарат №1", "Пильный аппарат №2", "Фрезер №3")

new_ids = f'''SELECT endpoints.id
FROM endpoints
WHERE name IN {facility_list}'''

ids_list = [id[0] for id in cursor.execute(new_ids)]

for id in ids_list:
    cursor.execute(f'''
                    INSERT INTO endpoint_groups (endpoint_id,  name)
                    VALUES ("{id}", "Цех №2")
                    ''')
connection.commit()
