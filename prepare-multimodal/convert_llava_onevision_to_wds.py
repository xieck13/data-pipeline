import json
import os
import webdataset as wds
import pandas as pd

from tqdm import tqdm
import glob

llava_pretrain_dir = '<path_to_LLaVA-Pretrain>'
output_llava_pretrain_dir = '<path_to_output_LLaVA-Pretrain>'

os.makedirs(output_llava_pretrain_dir, exist_ok=True)

parquet_files = glob.glob(os.path.join(llava_pretrain_dir, "*", '*.parquet'))

# Paths to the dataset files
output = os.path.join(output_llava_pretrain_dir, 'wds')

if not os.path.exists(output):
    os.mkdir(output)


with wds.ShardWriter(os.path.join(output, 'pretrain-%d.tar'), maxcount=10000) as shard_writer:

    for file in tqdm(parquet_files):
        df = pd.read_parquet(file)
        for index, row in df.iterrows():
            sample = {
                "__key__": row['id'],
                "jpg": row['image']['bytes'],
                "json": json.dumps(row['conversations']).encode("utf-8"),
            }
            shard_writer.write(sample)

print(f"Dataset successfully converted to wds")