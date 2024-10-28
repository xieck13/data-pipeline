import json
import os
import webdataset as wds
import pandas as pd

from tqdm import tqdm
import glob

from collections import defaultdict

import traceback

llava_pretrain_dir = './onevision'
output_llava_pretrain_dir = './onevision_wds'

os.makedirs(output_llava_pretrain_dir, exist_ok=True)

parquet_paths = glob.glob(os.path.join(llava_pretrain_dir, "*", "*.parquet"))
# Paths to the dataset files
output = os.path.join(output_llava_pretrain_dir, 'train')
os.makedirs(output, exist_ok=True)
error_path = defaultdict(int)
count = 0

with wds.ShardWriter(os.path.join(output, 'pretrain-%d.tar'), maxcount=10000) as shard_writer:
    for path in tqdm(parquet_paths):
        print(error_path[path])
        df = pd.read_parquet(path)
        for i, row in df.iterrows():
            conv = row['conversations'].tolist()
            for conv_id in range(0, len(conv), 2):
                try:
                    context = conv[conv_id]['value']
                    answers = conv[conv_id + 1]['value']
                    image = row['image']['bytes']
                    key = row['id'].replace('.', '_').replace('/', '_')
                    sample = {
                        "__key__": key + f"_{conv_id}",
                        "image": image,
                        "context": context,
                        "answers": answers,
                    }
                    shard_writer.write(sample)
                    count += 1
                    if count % 10000 == 0:
                        print(f"Processed {count} samples")
                except Exception as e:
                    error_path[path] += 1
                    traceback.print_exc()

print(f"Total samples: {count}")
print(f"Dataset successfully converted to wds")