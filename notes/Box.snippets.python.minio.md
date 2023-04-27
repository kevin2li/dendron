---
id: q7sf2b16rvom2rdaq55dab1
title: minio
desc: ''
updated: 1682582415261
created: 1682582343471
---

# 功能
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

# 设置图片的本地路径和在MinIO服务器上的存储路径
local_file = r"C:\Users\kevin\Downloads\Snipaste_2023-04-27_15-51-41.png"
minio_file = "Snipaste_2023-04-27_15-51-41.png"

# 上传图片到MinIO服务器
try:
    minio_client.fput_object( "image-bed", minio_file, local_file )
    print(f"{local_file} uploaded as {minio_file}")
except S3Error as e:
    traceback.print_exc()

```