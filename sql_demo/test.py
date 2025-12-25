import pymysql

# 链接数据库
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    db="test_db",
    charset="utf8",
)
# 配置结果以字典形式返回
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

print(f"链接数据库成功")

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS user (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  age INT
)
"""
)

data = [
    ("李四", 20),
    ("王五", 22),
]

cursor.executemany("INSERT INTO user (name, age) VALUES (%s, %s)", data)


cursor.execute("SELECT * FROM user")
res = cursor.fetchall()

print(f"user table is:\n{res}")
