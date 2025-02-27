#!/bin/bash
export HF_ENDPOINT="http://hf-mirror.com"

# 获取参数
REMOTE_REPO="LLM360/TxT360"
LOCAL_DIR="/media/xieck13/Elements/TxT360"
INCLUDE_PATTERN="data/common-crawl/*"

# 定义要执行的命令
COMMAND="huggingface-cli download --repo-type dataset --resume-download $REMOTE_REPO --local-dir $LOCAL_DIR --include $INCLUDE_PATTERN"

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
