import sqlite3
connection = sqlite3.connect("client.sqlite")
cursor = connection.cursor()
facility_list = ("Сварочный аппарат №1", "Пильный аппарат №2", "Фрезер №3")

reasons_request = '''SELECT DISTINCT reason_name, reason_hierarchy
FROM endpoint_reasons LEFT JOIN
endpoints ON endpoint_id = endpoints.id
WHERE name IN ("Фрезерный станок", "Старый ЧПУ", "Сварка")'''

new_ids = f'''SELECT endpoints.id
FROM endpoints
WHERE name IN {facility_list}'''

ids_list = [id[0] for id in cursor.execute(new_ids)]
reasons_list = tuple(cursor.execute(reasons_request))
for id in ids_list:
    for reason in reasons_list:
        cursor.execute(f'''
                        INSERT INTO endpoint_reasons
                        (endpoint_id,  reason_name, reason_hierarchy)
                        VALUES ("{id}", "{reason[0]}", "{reason[1]}")
                        ''')
connection.commit()
