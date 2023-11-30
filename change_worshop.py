import sqlite3
connection = sqlite3.connect("client.sqlite")
cursor = connection.cursor()
facility_list = ("Пильный станок", "Старый ЧПУ")

id_request = f'''SELECT id
FROM endpoints
WHERE name IN {facility_list}'''

ids_tuple = tuple(id[0] for id in cursor.execute(id_request))

cursor.execute(f'''UPDATE endpoint_groups
                SET name = 'Цех №2'
                WHERE endpoint_id IN {ids_tuple}''')
connection.commit()
