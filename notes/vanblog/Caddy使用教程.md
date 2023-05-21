# 简介
Caddy是一款基于Go语言编写的强大且可扩展的平台，可以给你的站点、服务和应用程序提供服务。可以将其看作Nginx的替代品之一，但是配置却更加简单方便，且支持自动HTTPS。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/fbb3ccc9560a60489346f841f72b063b.image.png)

官网： https://caddyserver.com/ 
文档：https://caddyserver.com/docs/  

<!-- more -->

# 安装
> 参考： https://caddyserver.com/docs/install

## Ubuntu安装
```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```
其他系统平台安装参见文档。

# 使用

:::tip{title="提示"}
需要先将DNS的A/AAAA记录指向服务器的公网IP，这样caddy会自动为指定的主机名申请ssl证书
:::

## 命令行方式
```bash
# 设置文件服务器
$ caddy file-server
# 指定域名
$ caddy file-server --domain example.com
# 设置反向代理
$ caddy reverse-proxy --from example.com --to localhost:9000
```

## Caddyfile方式
**启动**(与Caddyfile同一目录下执行)：  
`caddy run`  

:::tip{title="服务方式运行(推荐)"}
caddy也提供了系统服务运行方式，方便管理  
需要将配置写入`/etc/caddy/Caddyfile`    
启动： `sudo systemctl start caddy`
:::

- 单站点
```yaml
example.com

# Templates give static sites some dynamic features
templates

# Compress responses according to Accept-Encoding headers
encode gzip zstd

# Make HTML file extension optional
try_files {path}.html {path}

# Send API requests to backend
reverse_proxy /api/* localhost:9005

# Serve everything else from the file system
file_server
```

- 配置多站点
```yaml
# 单host
app1.example.com {
    reverse_proxy 127.0.0.1:10010
}

# 多host
:80, example.com, app2.example.com{
    reverse_proxy 127.0.0.1:10011
}

# 带路径
example.com, app2.example.com{
    reverse_proxy /api/* 127.0.0.1:10011
}

# 多node
example.com, app2.example.com{
    reverse_proxy 127.0.0.1:10011, 10.0.1.1:10011, 10.0.1.2:10011
}


```

## API方式
```json
POST /config/

{
  "apps": {
    "http": {
      "servers": {
        "example": {
          "listen": ["127.0.0.1:2080"],
          "routes": [{
            "@id": "demo",
            "handle": [{
              "handler": "file_server",
              "browse": {}
            }]
          }]
        }
      }
    }
  }
}
```

# 进阶
## 添加网页认证
参考：https://caddyserver.com/docs/caddyfile/directives/basicauth#basicauth

在反向代理中使用示例：
```json
app.example.com {
    encode gzip
    basicauth / {
        Bob $2a$14$Zkx19XLiW6VYouLHR5NmfOFU0z2GTNmpkT/5qqR7hx4IjWJPDhjvG
    }
    reverse_proxy 127.0.0.1:9000
}
```
注意：配置文件中不支持明文密码，需要使用`caddy hash-password`命令对密码加密后填入配置文件中。
