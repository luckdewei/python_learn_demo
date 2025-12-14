# test_flask_mysql_fixed.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text  # 导入 text
import pymysql

# 让 SQLAlchemy 使用 pymysql（如果使用 pymysql）
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 配置数据库连接 - 根据实际情况修改
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:123456@localhost:3306/test"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True  # 显示 SQL 语句，调试用

db = SQLAlchemy(app)


def test_flask_mysql():
    try:
        with app.app_context():
            # 修正：使用 text() 包装 SQL 语句
            db.session.execute(text("SELECT 1"))
            print("✅ Flask-SQLAlchemy 连接成功！")

            # 修正：所有 SQL 字符串都需要 text() 包装
            version_result = db.session.execute(text("SELECT VERSION()")).fetchone()
            print(f"MySQL 版本: {version_result[0]}")

            # 列出所有数据库
            databases = db.session.execute(text("SHOW DATABASES")).fetchall()
            print("所有数据库:")
            for db_name in databases:
                print(f"  - {db_name[0]}")

        return True

    except Exception as e:
        print(f"❌ Flask-SQLAlchemy 连接失败: {e}")
        return False


if __name__ == "__main__":
    test_flask_mysql()
