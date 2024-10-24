

下载ossctl，用于上传目录到oss
```bash
curl -LO https://oss-ap-southeast.scitix.ai/scitix/packages/ossctl/latest/linux-amd64/ossctl && chmod +x ossctl
```

添加ak，sk到config
```bash
# ./ossctl config add <配置名> https://oss-cn-north1.siflow.cn <AK> <SK>
./ossctl config add test_config https://oss-cn-north1.siflow.cn E4PVN2c9q3PBH0AeNTbm RkKEWNysdaBA8g8Iwfan
```


复制操作
```bash
# ./ossctl cp -r <本地路径> <配置名>/<bucket名>/<远程路径>

./ossctl cp -r ./InfiMM-WebMath-images/ test_config/tenant0814-test/InfiMM-WebMath-images-test
./ossctl cp -r test_config/tenant0814-test/InfiMM-WebMath-images-test ./InfiMM-WebMath-images/ 
```