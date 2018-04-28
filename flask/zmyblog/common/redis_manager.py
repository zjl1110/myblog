# -*- coding: utf-8 -*-
#__author__="ZJL"

import redis

# redisIP
redis_host = "127.0.0.1"

# redis端口
redis_port = 6379

# redisDB
redis_db = 0

# 连接
pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=redis_db)
# 连接池
r = redis.StrictRedis(connection_pool=pool)

# 可以设置过期时间的数据，seconds参数是过期时间
def setTimeData(key, seconds, value):
    r.setex(key,seconds, value)

# 取数据
def getData(keyname, coding="utf-8"):
    data = r.get(keyname)
    if data:
        data = data.decode(coding)
        return data
    else:
        return data