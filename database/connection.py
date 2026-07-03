import mysql.connector


class DataBaseConnection:
    def __init__(
        self, host="localhost", user="root", password="123454321", database="school"
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
