from flask import Flask, request, jsonify
from dbutils.pooled_db import PooledDB
import pymysql

# 创建链接池
POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True, # 链接用完是否阻塞
    host='127.0.0.1',
    port=3306,
    user='root',
    password=123456,
    database='test_db',
    charset='utf8mb4',
)

def fetch_one(sql, params=None):
    conn = POOL.connection()
    try:
        conn.begin()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchone()
        cursor.commit()
        print(f"result: {result}")
    except pymysql.err.OperationalError:
        conn.rollback()
        raise
    finally:
        conn.close() # 放回链接池



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
