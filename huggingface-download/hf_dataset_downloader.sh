#!/bin/bash

# 检查参数数量
if [ "$#" -ne 2 ]; then
    echo "Usage: \$0 <remote-repo> <local-dir>"
    exit 1
fi

# 获取参数
REMOTE_REPO=\$1
LOCAL_DIR=\$2

# 定义要执行的命令
COMMAND="huggingface-cli download --repo-type dataset --resume-download $REMOTE_REPO --local-dir $LOCAL_DIR"

# 无限循环，直到命令成功执行
while true; do
    # 执行命令
    $COMMAND
    
    # 检查命令是否成功
    if [ $? -eq 0 ]; then
        echo "Download completed successfully!"
        break
    else
        echo "Download failed, retrying in 5 seconds..."
        sleep 5
    fi
done
