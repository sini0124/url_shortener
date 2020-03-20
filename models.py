import pymysql
from DBUtils.PooledDB import PooledDB
import os
from dotenv import load_dotenv


load_dotenv(verbose=True)

POOL = PooledDB(
    creator=pymysql,  # Modules using linked databases
    maxconnections=6,
    # Maximum number of connections allowed by connection pool, 0 and None denote unrestricted number of connections
    mincached=2,
    # At the time of initialization, at least an idle app is created in the app pool. 0 means no app is created.
    maxcached=5,  # The maximum number of idle links in the app pool, 0 and None are unrestricted
    maxshared=3,
    # The maximum number of shared links in the app pool, 0 and None represent all shared links. PS: It's useless, because the threadsafe of modules like pymysql and MySQLdb are all 1. No matter how many values are set, _maxcached is always 0, so all links are always shared.
    blocking=True,
    # If there is no connection available in the connection pool, whether to block waiting. True, wait; False, don't wait and report an error
    maxusage=None,  # The maximum number of times a app is reused. None means unlimited.
    setsession=[],
    # A list of commands executed before starting a session. For example: ["set datestyle to...", "set time zone..."]
    ping=0,
    # ping MySQL On the server side, check if the service is available.# For example: 0 = None = never, 1 = Default = when it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host = os.getenv('HOST_NAME'),
    port = os.getenv('PORT_NUM'),
    user = os.getenv('USER_NAME'),
    password = os.getenv('PASSWORD'),
    db='test',
    charset='utf8',
    autocommit=True
)


class SQLHelper(object):

    @staticmethod
    def fetch_one(sql,args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def add_one(sql,args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.close()

    @staticmethod
    def remove_one(sql,args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.close()

    @staticmethod
    def update_one(sql,args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.close()