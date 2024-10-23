# -*- coding:utf-8 -*-
# @Time: 2022/12/21 20:58
# @Author: willian
# @File：add_task.py
# @desc: 读取laion5b的parquet文件添加到redis的任务队列


import os
import json
import time
import redis
import pandas as pd
import setting as se

from loguru import logger

from setting import RedisKey
import hashlib

logger_format = "{time:YYYY-MM-DD HH:mm:ss,SSS} [{thread}] {level} {file} {line} - {message}"

redis_client = redis.Redis(host=se.redis_ip, port=se.redis_port, db=se.redis_db, password=se.redis_pass, encoding="utf-8", decode_responses=True)
task_key = RedisKey.task_key
count_all = RedisKey.count_all

def hash_url(url):
    # 使用 SHA-256 哈希算法
    hash_object = hashlib.sha256(url.encode('utf-8'))
    # 返回十六进制的哈希值
    return hash_object.hexdigest()

def add_task():
    logger.add("./logs/add_task/add_task_{time:YYYY-MM-DD}.log", format=logger_format, level="INFO", rotation="00:00",
               retention='60 days')
    part_done = set()
    done_path = se.done_path
    if os.path.exists(done_path):
        with open(done_path, "rb") as f:
            for line in f:
                if line:
                    part_done.add(line.strip().decode())
    while True:
        if redis_client.llen(task_key) > se.addtask_threshold:
            time.sleep(10*60)
            continue
        base_path = se.parquet_dir
        # TODO glob the parquet file
        filename = "/volume/datacopy/InfiMM-WebMath-40B/part-00000-d02d03ca-9d67-4b41-ae48-a1ec4116ea42-c000.gz.parquet"
        df = pd.read_parquet(filename)
        rows = df.shape[0]
        # redis_client.incr(count_all, rows)       # 总数统计
        logger.info(f"开始添加task任务， task数：{rows}   part_file: {filename}")
        # #  Index(['id','SAMPLE_ID', 'URL', 'TEXT', 'HEIGHT', 'WIDTH', 'LICENSE', 'NSFW', 'similarity', 'image_suffix'], dtype='object')
        for index, row in df.iterrows():
            image_list = row.get("image_list")
            for img_url in image_list:
                if img_url is None:
                    continue
                image_id = hash_url(img_url)
                img_path = f"{image_id}.jpg"
                task_json = {"img_path": img_path, "img_url": img_url, "file_name": filename}
                logger.debug(f"添加任务：{task_json}")
                task_str = json.dumps(task_json)
                redis_client.lpush(task_key, task_str)
        logger.info(f"任务添加完成， task数：{rows}   part_file: {filename}")
        with open(done_path, "ab+") as f:
            f.write(filename.encode())
            f.write(b"\n")
        part_done.add(filename)


if __name__ == '__main__':
    add_task()