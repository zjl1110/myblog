# -*-coding:utf-8 -*-  
__author__ = "ZJL"


from sqlalchemy import create_engine
import traceback


engine = create_engine('mysql+pymysql://root:root123456@localhost:3306/dbtest?charset=utf8',
                                    pool_size=20,
                                    max_overflow=100,
                                    pool_recycle=7200,
                                    pool_timeout=30)


def select_one(sql):
    connection = engine.connect()
    with connection.begin() as trans:
        try:
            a = connection.execute(sql)
            return a.first()
        except Exception as e:
            return traceback.format_exc()

def select_one_dict(sql, keys):
    connection = engine.connect()
    with connection.begin() as trans:
        try:
            a = connection.execute(sql)
            a = a.first()
            if len(keys) == len(a):
                data_dict = {}
                for k, v in zip(keys, a):
                    data_dict[k] = v
                return data_dict
            else:
                return False
        except Exception as e:
            return traceback.format_exc()

def select_all(sql):
    connection = engine.connect()
    with connection.begin() as trans:
        try:
            a = connection.execute(sql)
            return a.fetchall()
        except Exception as e:
            return traceback.format_exc()

def select_all_dict(sql, keys):
    connection = engine.connect()
    with connection.begin() as trans:
        try:
            a = connection.execute(sql)
            a = a.fetchall()
            lists = []
            for i in a:
                if len(keys) == len(i):
                    data_dict = {}
                    for k, v in zip(keys, i):
                        data_dict[k] = v
                    lists.append(data_dict)
                else:
                    return False
            return lists
        except Exception as e:
            return traceback.format_exc()

def count_one(sql):
    connection = engine.connect()
    with connection.begin() as trans:
        try:
            a = connection.execute(sql)
            a = tuple(a.first())
            if isinstance(a, tuple) and a:
                return a[0]
            else:
                return False
        except Exception as e:
            return traceback.format_exc()

# 自动提交和回滚
def add_update_del(sql):
    connection = engine.connect()
    with connection.begin() as trans:
        try:
            connection.execute(sql)
            # connection.commit()
            return True
        except Exception as e:
            # connection.rollback()
            return traceback.format_exc()

