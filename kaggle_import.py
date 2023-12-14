import psycopg2
from datetime import datetime
import csv

username = 'postgres'
password = '3421'
database = 'lab5_DB'

import_rage = 10000

csv_file_path = "anime.csv"

def main():
    conn = psycopg2.connect(user=username, password=password, dbname=database)
    cursor = conn.cursor()

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        id = 0
        for row in csv_reader:
            id += 1
            anime_id, name, genre, anime_type, episodes, rating, members = row
            if episodes == "Unknown":
                episodes = 1
            if rating == "":
                rating = 5.0

            cursor.execute("insert into Animation_studio (studio_id, founded, country, name) values (%s, %s, %s, %s) returning studio_id",
                           (id, datetime.now().date(), 'Country', 'Studio Name'))

            cursor.execute("insert into Anime (name, type, episodes, rating, members, anime_id, studio_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (name, anime_type, episodes, rating, members, anime_id, id))

            if "," in genre:
                genres = {genre.strip() for genre in genre.split(',')}
            else:
                genres = {genre.strip()}
            for g in genres:
                cursor.execute("insert into Anime_genre (genre, anime_id) values (%s, %s)", (g, anime_id))
            if id == import_rage:
                break

    conn.commit()

    cursor.close()
    conn.close()

def clear_tables():
    conn = psycopg2.connect(user=username, password=password, dbname=database)
    cursor = conn.cursor()

    cursor.execute("delete from Anime_genre")
    cursor.execute("delete from Anime")
    cursor.execute("delete from Animation_studio")

    conn.commit()

    cursor.close()
    conn.close()

clear_tables()
main()