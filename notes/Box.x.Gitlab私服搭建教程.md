---
id: ttabxboou07jrozovi8b37r
title: Gitlab私服搭建教程
desc: ''
updated: 1684818185284
created: 1684732293880
---

## 简介
xx

## 方法
### 裸机安装
> 参考：https://about.gitlab.com/install/#ubuntu

``` bash 

sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl


curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

```
todo: 未完成

### docker安装
> 参考：https://docs.gitlab.com/ee/install/docker.html

1. 设置`GITLAB_HOME`环境变量
``` bash 
export GITLAB_HOME=$HOME/gitlab

# 写入shell's profile
echo "export GITLAB_HOME=$HOME/gitlab" >> ~/.zshrc
```
2. 使用docker-compose安装

注意将域名改为自己的.
``` yaml 
version: '3.6'
services:
  web:
    image: 'gitlab/gitlab-ce:latest'
    restart: always
    hostname: 'gitlab.example.com'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.example.com'
        # Add any other gitlab.rb configuration here, each on its own line
    ports:
      - '6080:80'
      - '6443:443'
      - '6022:22'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    shm_size: '256m'
```

启动:
``` bash 
docker compose up -d
```
3. 域名访问配置
- 域名可解析

- 内网穿透

- 反向代理

nginx:

``` nginx
# gitlab
server {
    server_name gitlab.kevin2li.top;
    listen 443 ssl http2;
    ssl_certificate /etc/nginx/ssl/kevin2li.top/fullchain.cer;
    ssl_certificate_key /etc/nginx/ssl/kevin2li.top/kevin2li.top.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    
    # listen 80 default;
    listen 80;
    if ($scheme = http) {
        return 301 https://$host:443$request_uri;
    }

    location / {
        proxy_pass http://127.0.0.1:5080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $http_host;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection upgrade;
        proxy_set_header Accept-Encoding gzip;
        proxy_redirect http:// https://;
    }
} 

```
4. 访问  

`https://gitlab.example.com`

- 用户名: `root`
- 密码: 通过下面命令行查看
``` bash 
sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

注意:

第一次登录建议用管理员root账号登录,否则会出现下面的警告:

![](https://minio.kevin2li.top/image-bed/blog/20230522224543.png)

可以在root登录后,设置界面取消勾选管理员同意注册选项.
![](https://minio.kevin2li.top/image-bed/blog/20230522224819.png)

或者同意新注册的用户:

![](https://minio.kevin2li.top/image-bed/blog/20230523102457.png)
