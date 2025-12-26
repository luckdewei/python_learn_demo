from extensions import pool
import pymysql


class UserModel:

    @staticmethod
    def get_all():
        conn = pool.connection()
        try:
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM user")
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def create(name, age):
        conn = pool.connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user(name, age) VALUES (%s, %s)", (name, age))
        finally:
            conn.close()
