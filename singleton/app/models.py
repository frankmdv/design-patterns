from flask import current_app
import sqlite3


class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, url_connect=current_app.config["DATABASE_PATH"]):
        self._connection = sqlite3.connect(url_connect, check_same_thread=False)

    @property
    def connection(self):
        return self._connection

    def fetch_all(self, sentence):
        cursor = self._connection.cursor()
        cursor.execute(sentence)

        results = cursor.fetchall()

        cursor.close()

        return results

    def fetch_one(self, sentence):
        cursor = self._connection.cursor()
        cursor.execute(sentence)

        results = cursor.fetchone()

        cursor.close()

        return results

    def insert(self, sentence):
        cursor = self._connection.cursor()
        cursor.execute(sentence)

        self._connection.commit()

        cursor.close()
