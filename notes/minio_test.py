# %%
from minio import Minio
from minio.error import S3Error
import traceback
from pathlib import Path
import os
from tqdm import tqdm
# %%

# 设置MinIO服务器信息
client = Minio(
    "124.222.5.56:9200",
    access_key="SrI2ahMMG1EmlUQ0",
    secret_key="B6DxrOxLa0wCpgBh6qhTUJVjD0alzqkB",
    secure=False
)

def upload_file(local_path, bucket_name: str="image-bed", dir=None):
    # 设置图片的本地路径和在MinIO服务器上的存储路径
    p = Path(local_path)
    minio_file = f"{dir}/{p.name}"
    try:
        client.fput_object(bucket_name, minio_file, local_path)
    except S3Error as e:
        traceback.print_exc()

# %%
# upload_file(r"C:\Users\kevin\Downloads\Snipaste_2023-04-27_18-21-09.png", dir="vanblog/img")
# %%
local_dir = r"C:\Users\kevin\images\img"
imgs = os.listdir(local_dir)
print(imgs)
# %%

objects = client.list_objects('image-bed', prefix="vanblog/img/", recursive=True)
# print(len(list(objects)))
objs = []
for obj in objects:
    obj_name = Path(obj.object_name)
    objs.append(obj_name.name)
print(objs)
# %%
left = set(imgs).difference(set(objs))
len(left)
# %%
for name in tqdm(left):
    upload_file(Path(local_dir) / name, dir='vanblog/img')
# %%
