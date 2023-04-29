---
id: q7sf2b16rvom2rdaq55dab1
title: minio
desc: ''
updated: 1682738252233
created: 1682582343471
---

## 功能
上传文件到Minio对象存储服务

``` python
from minio import Minio
from minio.error import S3Error
import traceback

# 设置MinIO服务器信息
minio_client = Minio(
    "server_ip:port",
    access_key="xx",
    secret_key="xx",
    secure=False
)

# 上传文件到存储桶
def upload_file(local_path, bucket_name: str="image-bed", dir=None):
    p = Path(local_path)
    minio_file = f"{dir}/{p.name}"
    try:
        client.fput_object(bucket_name, minio_file, local_path)
    except S3Error as e:
        traceback.print_exc()

# 列出存储桶文件
objects = client.list_objects('image-bed', prefix="vanblog/img/", recursive=True)
objs = []
for obj in objects:
    obj_name = Path(obj.object_name)
    objs.append(obj_name.name)
print(objs)
```