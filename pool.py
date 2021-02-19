import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB



PY_MYSQL_CONN_DICT = {
    "host": 'localhost',
    "port": 3306,
    "user": 'root',
    "passwd": 'root',
    "db": 'mysql',
    'charset': 'utf8',

}


class SQLPoll(object):
    # docstring for DbConnection

    __poll = None

    def __init__(self):
        self.pool = self.__get_db()
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    @classmethod
    def __get_db(cls):
        if cls.__poll is None:
            cls.__poll = PooledDB(
                # creator=pymysql,
                # mincached=10,
                # maxconnections=100,
                creator=pymysql,  # 使用链接数据库的模块
                maxconnections=10,  # 连接池允许的最大连接数，0和None表示不限制连接数
                mincached=6,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
                maxshared=3,
                # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
                blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
                ping=0,
                # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
                **PY_MYSQL_CONN_DICT)
        return cls.__poll

    def fetch_all(self, sql, args=None):
        if args is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def fetch_one(self, sql, args=None):
        if args is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            result = self.cursor.lastrowid
        except Exception as e:
            print('sql:[{}]meet error'.format(sql))
            print(e.args[-1])
            self.conn.rollback()
            return ()
        return result

    def __close(self):
        self.cursor.close()
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close()

