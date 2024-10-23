# -*- coding:utf-8 -*-
# @Time: 2023/1/31 14:37
# @Author: willian
# @File：setting.py
# @desc:

# redis连接配置
redis_ip = "localhost"
redis_port = 6379
redis_db = 0
redis_pass = "****123***"


# 使用到的 redis key 配置信息
class RedisKey:
    task_key = "image_task"                 # 存放任务队列
    count_all = "image_count_all"         # 统计已经加入了多少
    error_key = "image_task_error"          # 下载失败的任务队列
    count_error = "image_count_error"     # 统计下载失败数
    count_succ = "image_count_succ"       # 统计下载完成数
    count_disk = "count_worker_disk"        # 监控磁盘使用量


# parquet 目录配置 add_task.py 使用  样例：/mnt/vdb/laion5b/parquet/laion1B-nolang/0000~0128.parquet  /mnt/vdb/laion5b/parquet/laion2B-en/0000~0128.parquet
parquet_dir = "/volume/datacopy/InfiMM-WebMath-40B"
# 添加任务时候队列中少于5000000 开始执行添加任务
addtask_threshold = 5000000
# 添加过后的parquet路径写入 done_part.txt
done_path = "./done_part.txt"


# monitor_disk.py  查看存储空间占用情况
monitor_disk = '/volume/datacopy'


# downloader.py  下载的图片存储的目录 后续会拼接 laion1B-nolang  laion1B-nolang 等目录
store_dir = "/volume/datacopy/InfiMM-WebMath-images"
# 这里设置磁盘使用阈值是5000 GB   单位：GB
stop_threshold = 5000
# 下载多线程数 默认：32
thread_num = 32

# save_error_task.py  本地持久化redis错误队列数据 根据需要是否持久化 一般要开启此程序 否则错误较多redis占用较高
store_error_dir = "./error_task/"