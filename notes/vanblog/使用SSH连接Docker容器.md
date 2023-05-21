有时候需要通过ssh连接到容器内部，具体操作流程如下：
1. 启动容器，设置好端口映射
- 方式一：docker-compose
```yaml
version: '3.9'
services:
    ubuntu:
        container_name: ubuntu
        image: ubuntu:20.04
        # environment: null
        ports:
            - "30303:30303/tcp" # 填写ssh连接端口
        #volumes: null
        stdin_open: true
        tty: true
        command: bash
        restart: "unless-stopped"
```
- 方式二：docker命令行
```bash
docker run -itd -p 30303:30303 ubuntu:20.04
```

<!-- more -->

2. 容器内安装`openssh-server`
```bash
docker exec -it ubuntu bash
apt-get update
apt-get install openssh-server
```
3. 修改sshd配置文件
```bash
# /etc/ssh/sshd_config
Port 30303 # 设置ssh连接端口，默认为22，与容器开放端口一致
PermitRootLogin yes # 允许root用户登录
```
4. 设置用户密码
```bash
passwd
```

5. 启动sshd服务
```bash
service ssh status
service ssh start
```
6. 外部主机通过ssh连接
```bash
ssh root@<宿主机IP> -p 30303
```