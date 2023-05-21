
# 方法
## 查看已有分区

```bash
sudo fdisk -l
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b233ef0a42882141cb88af0a989ee090.image.png)

<!-- more -->

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4763728822dde106c92e0f6802bf4c8b.image.png)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/92a873a2c363d3b75086d817284326fe.image.png)
## 分区管理

`fdisk`常用基本操作：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/8ab7c6380cefbcc8dee4bbdadd724eae.image.png)

### 查看信息
```bash
sudo fdisk /dev/sdb
```
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/f07720053278e366a7ed9502ef71d2a9.image.png)

### 新建分区

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1b826199f7fc89a1ec5ada979d4b5586.image.png)

注意：分区结束位置也可以采用`+100G`这种写法。

#### 分区格式化
新建好分区后还要进行格式化才能使用。

```bash
mkfs -t ext4 /dev/sdb3
```

### 删除分区

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ddc2cf84490aa10da4e3924bbc85d680.image.png)

### 修改分区类型

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/83ad6d0629555905571b199bfafbf7a1.image.png)

:::info{title="常用分区类型"}

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/41d986482f6d481feb98704f68b4c836.image.png)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/91d5c01dd9e31cd4d19d0397ec40ba78.image.png)
:::

