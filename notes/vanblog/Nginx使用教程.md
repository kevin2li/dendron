# 简介
Nginx是一个高性能的HTTP和反向代理web服务器，具有占有内存少，并发能力强等特点。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/91dcaa8515bc528fb886bcac4f00edf9.image.png)

官网：https://www.nginx.com/   
文档：https://www.nginx.com/resources/wiki/  

<!-- more -->


# 安装
> 参考：https://www.nginx.com/resources/wiki/start/topics/tutorials/install/

# 常用命令
```bash
nginx -t
nginx -s
```

# 常用配置
> 参考：[微信：看完这篇还不懂Nginx服务器配置，那我要哭了](https://mp.weixin.qq.com/s?__biz=MzU4ODI1MjA3NQ==&mid=2247505559&idx=2&sn=c885d30be2456658bf4d1a044e87f27b&chksm=fddd0053caaa89456dbff5ca37397deafdb54a7e2ccb1fcfd14ea4ac9853b5ff054319a6d7e9&mpshare=1&scene=1&srcid=0818gcbcfKBKRXQ2owHzviRb&sharer_sharetime=1660837414695&sharer_shareid=b44ebbe82718b61b6a9fa0be4bb87fab#rd)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/92d5a41ece12f2089d9648c5708353f3.image.png)

推荐配置举例：
配置文件位置：`/etc/nginx/nginx.conf`  
内容如下：
```yaml
load_module /usr/lib/nginx/modules/ngx_stream_module.so;
user www-data;
worker_processes auto;
pid /run/nginx.pid;
events {
    worker_connections  1024;
    accept_mutex on;
}
  
http {
  include mime.types;
  default_type application/octet-stream;
  keepalive_timeout 75s;
  gzip on;
  gzip_min_length 4k;
  gzip_comp_level 4;
  client_max_body_size 1024m;
  client_header_buffer_size 32k;
  client_body_buffer_size 8m;
  server_names_hash_bucket_size 512;
  proxy_headers_hash_max_size 51200;
  proxy_headers_hash_bucket_size 6400;
  gzip_types application/javascript application/x-javascript text/javascript text/css application/json application/xml;
  error_log /var/log/nginx/error.log;
  access_log /var/log/nginx/access.log;

  server {
    server_name blog.example.com;
    listen 443 default ssl http2;
    ssl_certificate *.cer;
    ssl_certificate_key *.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    listen 80 default;
    if ($scheme = http) {
      return 301 https://$host:443$request_uri;
    }
    location / {
      # blog;
      proxy_pass http://127.0.0.1:10011;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Host $http_host;
      proxy_set_header X-Forwarded-Port $server_port;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_redirect http:// https://;
    }
  }
}

stream {
  log_format basic '$remote_addr [$time_local] $protocol $status $bytes_sent $bytes_received $session_time "$upstream_addr" "$upstream_bytes_sent" "$upstream_bytes_received" "$upstream_connect_time"';
  access_log /var/log/nginx/stream_access.log basic;
  open_log_file_cache off;
}

```

# SSL证书申请与自动续签
> 参考： 
> 1. https://github.com/acmesh-official/acme.sh/wiki/%E8%AF%B4%E6%98%8E
> 2. https://github.com/acmesh-official/acme.sh

## 安装acme.sh
```bash
# 下载并安装
curl https://get.acme.sh | sh -s email=my@example.com

# (可选，创建别名方便使用)
alias acme.sh=~/.acme.sh/acme.sh
```
## 配置DNS API
- 腾讯云DNSPOD

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ee3622e1c31dc939cc489fa6c71d4127.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e54eb08f69113e8c057f5a20a10463db.image.png)

记录下申请的密钥的ID和Token值，并执行下面命令存到环境变量中
```bash
export DP_Id="123456"
export DP_Key="602abcd"
```

## 申请证书
- 腾讯云
```bash
# 为nginx申请证书(可多次使用-d选项，同时申请多个证书)
acme.sh --dns dns_dp --issue -d example.com --nginx

# 申请泛域名证书
acme.sh --dns dns_dp --issue -d "*.example.com"  -d example.com --nginx

# 为web root申请证书
acme.sh --dns dns_dp --issue -d example.com -d www.example.com --webroot /home/wwwroot/mydomain.com/

```

## 安装证书

:::warning{title="注意"}
默认生成的证书都放在安装目录下: ~/.acme.sh/, 请不要直接使用此目录下的文件, 例如: 不要直接让 nginx/apache 的配置文件使用这下面的文件. 这里面的文件都是内部使用, 而且目录结构可能会变化.
:::

- nginx
```bash
acme.sh --install-cert -d example.com \
--key-file       /path/to/keyfile/in/nginx/key.pem  \
--fullchain-file /path/to/fullchain/nginx/cert.pem \
--reloadcmd     "service nginx force-reload"
```

## 自动续签
acme安装成功后会自动为你创建 cronjob, 每天 0:00 点自动检测所有的证书, 如果快过期了, 需要更新, 则会自动更新证书。可通过`crontab -l`查看定时任务：


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6005f88273a3b369ef0b62d7d6d8eec2.image.png)
