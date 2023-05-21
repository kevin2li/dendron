# 方法
0. 先查看自己的硬盘是否被自动挂载
```bash
lsblk
```
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c6a060031303902d104d6df4594292a3.image.png)

<!-- more -->

可以通过查看挂载点目录判断自己的硬盘是否被挂载

1. 查看磁盘列表

```bash
sudo fdisk -l
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/46b5fee9a80bff9d52984f78f9c78fe4.image.png)

可以根据容量大小判断需要挂载的硬盘名称，后面会用到。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/9a979acc59d1bc997a71ea71b0e7d94b.image.png)

如我这里要挂载的磁盘是 `/dev/nvme0n1p3`

2. 挂载磁盘
```bash
# 创建挂载点目录(如已存在，可省略)
mkdir -p /media/kevin2li/System

# 挂载
sudo mount /dev/nvme0n1p3 /media/kevin2li/System
```
这样就挂载成功了。

可以通过`df -h`命令验证：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/8bf7856d612817d0321a8673a2195ace.image.png)

:::info{title="取消挂载"}
如果要取消挂载可以使用如下命令：
```bash
sudo umount /dev/nvme0n1p3
```
:::

3. 开机自动挂载

查看要挂载的磁盘的UUID和分区类型。
```bash
blkid /dev/nvme0n1p3
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2cdfc13ca50b1f5670cbd46a01bf6c60.image.png)

编辑`/etc/fstab`文件，在文件尾部追加一行(根据上面查到的信息修改)：
```bash
UUID=4E30F0C230F0B257 /media/kevin2li/System ntfs defaults 0 0
```

:::info{title="/etc/fstab字段说明"}

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6d99ff80165bdf82af9a8c1fa903df0c.image.png)

:::
重新加载：
```bash
sudo mount -a
```

# 参考
1. https://cloud.tencent.com/developer/article/1813949
2. https://www.simplified.guide/linux/disk-mount
