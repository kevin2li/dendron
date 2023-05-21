# 简介
Docker是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

Docker的核心是Docker引擎，它是一个轻量级的容器化技术，可以在Linux、Windows和Mac上运行。Docker引擎可以将应用程序及其依赖项打包到一个可移植的容器中，从而实现快速部署、可移植性和可伸缩性。Docker引擎还提供了一组API，可以用于管理和监视容器。

**Docker镜像生命周期：**
![640.jpg](https://minio.kevin2li.top/image-bed/vanblog/img/55f78e2df8a5e9d5f1044eab3792e4ef.640.jpg)


官网：https://www.docker.com/  
engine文档：https://docs.docker.com/engine/   
Dockerfile文档： https://docs.docker.com/engine/reference/builder/  
compose-file文档：https://docs.docker.com/compose/compose-file/05-services/  

<!-- more -->

# 安装
- Ubuntu  
参考：[Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
```bash
# 卸载旧版本
sudo apt-get remove docker docker-engine docker.io containerd runc

# 安装相关依赖包
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release

# 添加GPG key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 设置repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 安装
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# 常用命令
## 镜像管理
```bash
# 构建镜像(位于Dockerfile目录下)
docker build -t my/image .

# 拉取镜像
docker pull nginx

# 上传镜像
docker push myimage:1.0

# 删除镜像
docker rmi nginx

# 列出镜像
docker images

# 给镜像打标签(参数1为镜像，参数2为新标签名)
docker tag ubuntu ubuntu:18.04

# 导出镜像
docker save -o nginx.tar nginx

# 导入镜像
docker load -i nginx.tar
````
## 容器管理
```bash
# 启动容器
docker run -it -d -p 8080:80 --name nginx --rm -v /data:/data -e PASSWORD=123456 --network mynet nginx

# 停止容器
docker stop nginx

# 启动停止后的容器
docker start nginx

# 删除容器
docker rm nginx

# 查看当前运行容器
docker ps

# 查看所有容器
docker ps -a

# 进入容器
docker exec -it nginx /bin/bash

# 宿主机与容器文件移动
docker cp /home/user/a.txt nginx:/data/

# 提交容器为镜像
docker commit nginx

# 查看容器信息
docker inspect nginx

# 查看容器日志
docker logs nginx

# 查看所有运行容器状态
docker stats

# 查看容器内进程状态
docker top nginx

# 查看容器映射端口
docker port nginx

# 容器导出
docker export -o nginx.tar nginx

# 容器导入
docker import nginx.tar nginx

```
## 网络管理
```bash
# 创建网络
docker network -d bridge mynet

# 列出网络
docker network ls

# 删除网络
docker network rm mynet

# 将容器连接至网络
docker network connect mynet nginx

# 将容器断开网络
docker network disconnect mynet nginx
```

## 数据卷管理
```bash
# 创建数据卷
docker volume create myvol

# 列出数据卷
docker volume ls

# 查看数据卷
docker volume inspect myvol

# 删除数据卷
docker volume rm myvol
```

# 配置
## 镜像加速
参考： https://blog.kevin2li.top/post/60


