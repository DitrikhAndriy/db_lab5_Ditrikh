import csv
import psycopg2

username = 'postgres'
password = '3421'
database = 'lab5_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cursor = conn.cursor()

tables = ["Animation_studio", "Anime", "Anime_genre"]

for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    csv_file_path = f"{table}.csv"

    with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow([desc[0] for desc in cursor.description])

        csv_writer.writerows(rows)