
# 方法

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c750aa74bc05eb060e922a00ec9fe18c.image.png)

## 第一次设置
```bash
# 1. 查看是否已有swap文件
swapon -s

# 2. 没有则创建swap文件
dd if=/dev/zero of=/usr/swap/swapfile bs=1M count=4096

# 3. 创建的空文件转化为swap格式
mkswap /usr/swap/swapfile

# 4. 启用swap文件
swapon /usr/swap/swapfile

# 5. 开机自动启用该文件(在/etc/fstab文件最后一行添加)
/usr/swap/swapfile swap swap defaults 0 0
```

## 修改设置
```bash
# 关闭swap文件
swapoff /usr/swap/swapfile

# 重新分配大小
dd if=/dev/zero of=/usr/swap/swapfile bs=1M count=4096

# 后面同上面第3步及之后
```
<!-- more -->

# 参考
Source: Conversation with Bing, 2023/3/5  

(1) [Linux设置虚拟内存 - 腾讯云开发者社区-腾讯云. https://cloud.tencent.com/developer/article/1704157  

(2) Linux设置虚拟内存 - 天马行宇 - 博客园. https://www.cnblogs.com/yuanyongqiang/p/15650176.html 

(3) 【Linux】设置虚拟内存_星河_赵梓宇的博客-CSDN博客. https://blog.csdn.net/Aria_Miazzy/article/details/100532714  

(4) 虚拟内存设置（解决linux内存不够情况） - 玩过熊 - 博客园. https://www.cnblogs.com/gethinwang/p/10511047.html  

(5) 怎样设置虚拟内存？-百度经验. https://jingyan.baidu.com/article/2fb0ba4075567800f2ec5fcb.html   

(6) ubuntu下配置虚拟内存_i-Curve的博客-CSDN博客. https://blog.csdn.net/qq_38701476/article/details/83042668  
