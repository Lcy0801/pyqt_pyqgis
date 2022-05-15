# 封装对access数据库相关的操作
import pypyodbc
def mdb_conn(db_name, password=""):
    """
    :param db_name:s数据库名称
    :param password:数据库密码
    :return:返回数据库连接
    """
    connstr = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};PWD=' + \
          password + ";DBQ=" + db_name  # 创建连接数据
    conn = pypyodbc.win_connect_mdb(connstr)
    return conn
