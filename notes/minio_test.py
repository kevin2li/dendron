from minio import Minio
from minio.error import S3Error
import traceback

# 设置MinIO服务器信息
minio_client = Minio(
    # "minio.kevin2li.top",
    "127.0.0.1:9999",
    access_key="SrI2ahMMG1EmlUQ0",
    secret_key="B6DxrOxLa0wCpgBh6qhTUJVjD0alzqkB",
    secure=True
)

# 设置图片的本地路径和在MinIO服务器上的存储路径
local_file = r"C:\Users\kevin\Downloads\Snipaste_2023-04-27_13-29-34.png"
minio_file = "images/image.png"

# 上传图片到MinIO服务器
try:
    with open(local_file, "rb") as file_data:
        print(file_data)
        minio_client.put_object(
            bucket_name="image-bed",
            object_name=minio_file,
            data=file_data,
            length=file_data.seek(0, 2),
            content_type="image/jpeg"
        )
    print(f"{local_file} uploaded as {minio_file}")
except S3Error as e:
    traceback.print_exc()
