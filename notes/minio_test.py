from minio import Minio
from minio.error import S3Error
import traceback

# 设置MinIO服务器信息
client = Minio(
    "124.222.5.56:9200",
    access_key="SrI2ahMMG1EmlUQ0",
    secret_key="B6DxrOxLa0wCpgBh6qhTUJVjD0alzqkB",
    secure=False
)

# # 设置图片的本地路径和在MinIO服务器上的存储路径
# local_file = r"C:\Users\kevin\Downloads\Snipaste_2023-04-27_15-51-41.png"
# minio_file = "Snipaste_2023-04-27_15-51-41.png"

# # 上传图片到MinIO服务器
# try:
#     client.fput_object( "image-bed", minio_file, local_file )
#     print(f"{local_file} uploaded as {minio_file}")
# except S3Error as e:
#     traceback.print_exc()

# List all object paths in bucket that begin with my-prefixname.
objects = client.list_objects('image-bed', recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)

# List all object paths in bucket that begin with my-prefixname using
# V2 listing API.
# objects = client.list_objects_v2('image-bed', prefix='',
#                                  recursive=True)
# for obj in objects:
#     print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
#           obj.etag, obj.size, obj.content_type)
