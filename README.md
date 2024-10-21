# data-pipeline

## Check list

- [ ] Download image @congkai
  - [ ] 反爬代理+下载数据
- [ ] Parser（Resiliparse/Trafilatura） @kejing
- [ ] Filter
  - [ ] Fasttext @kejing
    - [ ] 数据构造（包括tokenize）
    - [ ] 训练
    - [ ] 推理（based on spark）
  - [ ] Rule filter @all
- [ ] Dedup @congkai
  - [ ] minhash
  - [ ] substr
  - [ ] text
  - [ ] cluster-based
- [ ] LLM/MLLM infer 
  - [ ] 模型评估 （现成）
  - [ ] 标注数据（vllm/sglang backend）@congkai
  - [ ] 计算loss/ppl @kejing
- [ ] LLM/MLLM trainer @congkai
  - [ ] 1B模型训练
