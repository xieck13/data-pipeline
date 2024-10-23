# start redis server
apt update && apt install -y redis

# 启动redis-server在daemon模式
redis-server --requirepass "****123***" --daemonize yes
