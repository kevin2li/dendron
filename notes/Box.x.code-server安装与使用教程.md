---
id: mnutg2mdtl6k29alw3vilx9
title: code-server安装与使用教程
desc: ''
updated: 1684659836953
created: 1684653637261
---


## 简介
Code-server是一个基于浏览器的开源项目，它将Visual Studio Code (VS Code)的开发环境以Web应用的形式提供。它允许您通过浏览器远程访问和使用VS Code的完整功能，无论您在何处，只要有网络连接，就可以使用自己喜欢的编辑器进行编码和开发。

下面是Code-server的一些主要特点和功能：

- **远程开发环境**：Code-server提供了一个完整的VS Code开发环境，包括语法高亮、代码补全、调试、版本控制等功能。您可以使用任何支持现代浏览器的设备访问Code-server，例如个人电脑、笔记本电脑、平板电脑等。
- 跨平台支持：Code-server可以运行在各种操作系统上，包括Windows、macOS和Linux。这使得您可以在不同的设备和操作系统上保持一致的开发环境。

- **可定制性**：Code-server支持大部分VS Code的扩展和插件，您可以根据需要安装和配置您喜欢的扩展，以满足特定的开发需求。它还提供了一些自定义选项，可以根据个人偏好进行界面和行为的调整。

- **协作和共享**：通过Code-server，您可以与他人协作开发，共享代码和项目。您可以与团队成员同时编辑和预览代码，通过浏览器实时交流和协作。

- **安全性**：Code-server提供了一些安全措施，包括访问控制和身份验证。您可以通过设置密码、使用SSL等方式来保护Code-server的访问和数据传输安全。

- **灵活的部署方式**：Code-server可以以自托管方式部署在您自己的服务器或本地环境中。您可以根据需要自定义部署方式，并根据实际需求进行扩展和配置。

Code-server为开发者提供了一种方便、灵活和跨平台的远程开发环境。无论是个人开发者还是团队协作，Code-server都可以提供一种无缝的开发体验，让您在任何地方都能获得高效的开发工具和环境。

文档：https://coder.com/docs/code-server/latest  
Github: https://github.com/coder/code-server

## 安装
- 一键脚本安装：

```bash
curl -fsSL https://code-server.dev/install.sh | sh
```
安装完成后，启动。

```bash
# 1. 现在启动并加入开机自启
sudo systemctl enable --now code-server@$USER

# 查看运行状态
sudo systemctl status code-server@$USER

# 2. 前台启动
code-server

# 3. 指定端口启动
PORT=8072 code-server

# or
code-server --bind-addr 127.0.0.1:8072
```

默认脚本会在8080端口提供服务，打开网页可以看到如下界面：

![](https://minio.kevin2li.top/image-bed/blog/20230521152655.png)

密码可在`~/.config/code-server/config.yaml`中查看。

登录成功后即可看到熟悉的vscode界面。

![](https://minio.kevin2li.top/image-bed/blog/20230521152903.png)


## 使用
### 导入profile
为了保持开发环境的一致性，可以将自己之前常用的配置直接导入到云开发环境中。

![](https://minio.kevin2li.top/image-bed/blog/20230521164607.png)

### 暴露服务

1. 使用内网穿透工具进行端口映射

如使用[nps](https://github.com/ehang-io/nps)将本地的8080端口映射到公网机器的8073端口。

![](https://minio.kevin2li.top/image-bed/blog/20230521161528.png)

2. nginx反向代理

我的公网机器映射端口为8072，访问域名为`code-cloud.kevin2li.top`。

nginx默认配置文件路径：`/etc/nginx/nginx.conf`

nginx参考配置如下：
```nginx
# code-cloud
server {
	server_name code-cloud.kevin2li.top;
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
		proxy_pass http://127.0.0.1:8073;
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
修改完后，测试并启用：
```bash
# 测试配置文件
sudo nginx -t

# 重新加载配置文件
sudo nginx -s reload
```

之后就可以通过你自定义的域名访问了。
