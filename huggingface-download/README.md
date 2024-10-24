# huggingface cli下载

一次下载
```bash
# 下载全部
huggingface-cli download --repo-type dataset --resume-download Infi-MM/InfiMM-WebMath-40B --local-dir InfiMM-WebMath-40B

# 下载部分（include或exclude）
huggingface-cli download --repo-type dataset --resume-download mlfoundations/MINT-1T-HTML --local-dir MINT-1T-HTML --include data_v1_1/shard_001*.parquet
```

反复下载
```bash
#!/bin/bash

# 定义要执行的命令
COMMAND="huggingface-cli download --repo-type dataset --resume-download Infi-MM/InfiMM-WebMath-40B --local-dir InfiMM-WebMath-40B"

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
```
