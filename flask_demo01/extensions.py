from dbutils.pooled_db import PooledDB
import pymysql
from config import Config

pool = PooledDB(creator=pymysql, maxconnections=10, autocommit=True, **Config.MYSQL)
