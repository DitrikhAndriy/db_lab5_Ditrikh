import json
import psycopg2
from datetime import date

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

username = 'postgres'
password = '3421'
database = 'lab5_DB'
host = 'localhost'
port = '5432'

json_filename = 'exported_data.json'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cursor = conn.cursor()

tables = ["Animation_studio", "Anime", "Anime_genre"]

data = {}

for table in tables:
    query = f"SELECT * FROM {table};"
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    table_data = []
    for row in rows:
        table_data.append(dict(zip(columns, row)))

    data[table] = table_data

with open(json_filename, 'w') as json_file:
    json.dump(data, json_file, indent=2, cls=DateEncoder)