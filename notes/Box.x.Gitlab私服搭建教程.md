---
id: ttabxboou07jrozovi8b37r
title: Gitlab私服搭建教程
desc: ''
updated: 1684825923002
created: 1684732293880
---

## 简介
GitLab是一个基于Web的Git代码仓库管理工具，类似于GitHub，但提供了更完整的应用程序生命周期管理解决方案，包括持续集成/持续交付（CI/CD）、问题跟踪、代码审查、代码片段等功能，可以帮助团队更高效地协作开发和部署应用程序。

GitLab有两个版本：社区版和企业版。社区版是免费的开源软件，可以自行搭建在本地服务器或云端，并提供了很多功能，如代码管理、问题跟踪、持续集成/持续交付（CI/CD）等。而企业版则提供了更多的高级功能，如代码审查、高可用性、容器注册表等，并提供了更多的安全和管理功能。

GitLab的主要特点包括：

代码管理：GitLab提供了一个易于使用的Web界面，可以管理代码仓库、分支、标记等，并提供了与Git兼容的版本控制功能。

持续集成/持续交付（CI/CD）：GitLab集成了CI/CD功能，可以自动构建、测试和部署应用程序，支持多种集成测试和部署环境，如Kubernetes、Docker等，并提供了丰富的插件和API。

问题跟踪：GitLab提供了问题跟踪功能，可以帮助团队跟踪和解决问题，如bug、任务、需求等，并支持多种问题状态、优先级、标签等。

代码审查：GitLab提供了代码审查功能，可以帮助团队进行代码评审和合并请求，并支持多种合并策略、审查标准、评论等。

代码片段：GitLab提供了代码片段功能，可以方便地分享和管理代码片段，并支持多种语言和格式。

安全和管理：GitLab提供了多种安全和管理功能，如用户和权限管理、LDAP集成、二步验证、防火墙、漏洞扫描等，可以帮助团队更好地保护应用程序和数据的安全。

总之，GitLab是一个功能齐全的代码仓库管理工具，可以帮助团队更高效地协作开发和部署应用程序，提高开发效率和质量。

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
    container_name: gitlab
    restart: always
    hostname: 'gitlab.kevin2li.top'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.kevin2li.top'
        # Add any other gitlab.rb configuration here, each on its own line
        gitlab_rails['gitlab_shell_ssh_port'] = 5022
        nginx['listen_port'] = 80
        nginx['listen_https'] = false
      TZ: Asia/Shanghai
    ports:
      - '5080:80'
      - '5443:443'
      - '5022:22'
    volumes:
      - '${PWD}/config:/etc/gitlab'
      - '${PWD}/logs:/var/log/gitlab'
      - '${PWD}/data:/var/opt/gitlab'
    shm_size: '256m'
```

启动:
``` bash 
docker compose up -d
```

可能需要等待一会才能正常运行,可以进入容器查看状态:
``` bash 
docker exec -it gitlab bash
# 查看状态
gitlab-ctl status

# 重启各项服务
gitlab-ctl reconfigure
```

当出现下面结果时,说明已经正常运行

![](https://minio.kevin2li.top/image-bed/blog/20230523142631.png)


3. 域名访问配置
- 域名可解析  
添加一条A记录,域名为`gitlab.kevin2li.top`,指向公网服务器ip.

- 内网穿透  
将服务器的`5022`端口映射到本地服务器的`5022`端口,并开放服务器的`5022`端口以供外部访问.
``` bash 
sudo systemctl --permanent --zone=public --add-port 5022/tcp
sudo systemctl --reload
```

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

之后就可以愉快的使用了.

# 参考
1. [Configure SSL for the GitLab Linux package ](https://docs.gitlab.com/omnibus/settings/ssl/#change-the-default-ssl-certificate-location)