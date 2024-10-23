# -*- coding:utf-8 -*-
# @Time: 2022/12/21 23:42
# @Author: willian
# @File：speed.py
# @desc:

import time
import redis
import setting

from setting import RedisKey

redis_client = redis.Redis(host=setting.redis_ip, port=setting.redis_port, db=setting.redis_db, password=setting.redis_pass, encoding="utf-8", decode_responses=True)


def speed():
    error = RedisKey.count_error
    succ = RedisKey.count_succ
    while True:
        s_c = int(redis_client.get(error)) + int(redis_client.get(succ))
        time.sleep(10)
        e_c = int(redis_client.get(error)) + int(redis_client.get(succ))
        c = e_c-s_c
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}   10秒钟处理：{c}  处理速率：{c/10}")


if __name__ == '__main__':
    speed()
