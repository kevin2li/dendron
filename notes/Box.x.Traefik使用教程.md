---
id: ls3l0rt2hv0pdyjyr1mkd8w
title: Traefik使用教程
desc: ''
updated: 1684981925565
created: 1684976834633
---
# 简介

![](https://minio.kevin2li.top/image-bed/blog/20230525093259.png)

文档：https://doc.traefik.io/traefik/routing/providers/docker/


## 教程

### traefik安装
`docker-compose.yml`:

```yaml
version: '3'

services:
  reverse-proxy:
    # The official v2 Traefik docker image
    image: traefik:v2.9
    # Enables the web UI and tells Traefik to listen to docker
    command: --api.insecure=true --providers.docker
    ports:
      # The HTTP port
      - "80:80"
      # The Web UI (enabled by --api.insecure=true)
      - "8080:8080"
    volumes:
      # So that Traefik can listen to the Docker events
      - /var/run/docker.sock:/var/run/docker.sock
```

启动成功后，本机访问`http://localhost:8080`可打开WebUI首页：

![](https://minio.kevin2li.top/image-bed/blog/2023-05-25_094809.png)

### 概念梳理

![](https://minio.kevin2li.top/image-bed/blog/20230525095349.png)

1. Providers  

Providers用于定义和管理不同类型的后端服务。它们提供了一种机制，让Traefik能够动态地发现和配置后端服务，从而实现自动化的负载均衡和反向代理。包括File Provider、Docker Provider、Kubernetes Provider等。

2. EntryPoints  

EntryPoints表示入口点，也就是访问Traefik的入口地址。EntryPoints定义了Traefik监听的端口和协议，例如HTTP、HTTPS和TCP等。可以为每个EntryPoints定义一个名称和一组配置。

配置示例：

`address`格式：`[host]:port[/tcp|/udp]`
``` yaml 
## Static configuration
entryPoints:
  web:
    address: ":80"

  websecure:
    address: ":443"
```

3. Routers  

Routers表示路由器，用于将请求路由到正确的服务。每个Router定义了匹配规则、请求头、路径、主机名等配置，以及要使用的中间件。

配置示例：
``` yaml 
## Dynamic configuration
http:
  routers:
    my-router:
      rule: "Host(`example.com`)"   # 根据主机名
      # rule: "Path(`/foo`)"        # 根据路径
      # rule: "Host(`example.com`) || (Host(`example.org`) && Path(`/traefik`))" # 组合条件

      # rule: Headers(`key`, `value`)   # 根据headers
      # rule: Method(`GET`, ...)        # 根据Method
      # rule: ClientIP(`10.0.0.0/16`, `::1`)  # 根据客户端IP
      service: service-foo
```

> 详细可参考：https://doc.traefik.io/traefik/routing/routers/

4. Middlewares

Middlewares用于定义和管理HTTP请求的中间件。它们提供了一种机制，让Traefik可以动态地修改或增强HTTP请求和响应，例如添加身份验证、重定向、日志记录等功能。

HTTP中间件：https://doc.traefik.io/traefik/middlewares/http/overview/
TCP中间件：https://doc.traefik.io/traefik/middlewares/tcp/overview/

配置示例：

BasicAuth中间件：

``` yaml 
# this is for docker
# Declaring the user list
#
# Note: when used in docker-compose.yml all dollar signs in the hash need to be doubled for escaping.
# To create user:password pair, it's possible to use this command:
# echo $(htpasswd -nB user) | sed -e s/\\$/\\$\\$/g
#
# Also note that dollar signs should NOT be doubled when they not evaluated (e.g. Ansible docker_container module).
labels:
  - "traefik.http.middlewares.test-auth.basicauth.users=test:$$apr1$$H6uskkkW$$IgXLP6ewTrSuBkTrqE8wj/,test2:$$apr1$$d9hr9HBB$$4HxwgUir3HP4EsggP/QNo0"
```

5. Services  

Services表示服务，是实际应用程序的后端。每个Service定义了应用程序的地址、端口、协议等配置。

配置示例：
``` yaml 
## Dynamic configuration
http:
  services:
    my-service:
      loadBalancer:
        servers:
        - url: "http://<private-ip-server-1>:<private-port-server-1>/"
        - url: "http://<private-ip-server-2>:<private-port-server-2>/"
```

### Docker容器配置
> 详见：https://doc.traefik.io/traefik/routing/providers/docker/

常用路由配置：  
| 名称                                                  | 含义         | 举例                                                        |
| ----------------------------------------------------- | ------------ | ----------------------------------------------------------- |
| `traefik.http.routers.<router_name>.rule`             | 匹配路由规则 | ``traefik.http.routers.myrouter.rule=Host(`example.com`)``  |
| `traefik.http.routers.<router_name>.entrypoints`      | 接入点       | `traefik.http.routers.myrouter.entrypoints=ep1,ep2`         |
| `traefik.http.routers.<router_name>.middlewares`      | 中间件       | `traefik.http.routers.myrouter.middlewares=auth,prefix,cb`  |
| `traefik.http.routers.<router_name>.service`          | 服务         | `traefik.http.routers.myrouter.service=myservice`           |
| `traefik.http.routers.<router_name>.tls`              | 使用tls      | `traefik.http.routers.myrouter.tls=true`                    |
| `traefik.http.routers.<router_name>.tls.certresolver` | tls证书      | `traefik.http.routers.myrouter.tls.certresolver=myresolver` |

常用服务配置：  
| 名称                                                            | 含义         | 举例                                                            |
| --------------------------------------------------------------- | ------------ | --------------------------------------------------------------- |
| `traefik.http.services.<service_name>.loadbalancer.server.port` | 指定服务端口 | `traefik.http.services.myservice.loadbalancer.server.port=8080` |
| `traefik.http.services.<service_name>.loadbalancer.server.scheme` | 指定协议 | `traefik.http.services.myservice.loadbalancer.server.scheme=http` |

实际案例：

1. 配置单个路由
``` yaml 
version: "3"
services:
  my-container:
    # ...
    labels:
      # 指定主机名
      - traefik.http.routers.my-container.rule=Host(`example.com`)
      # 指定连接端口号(不指定默认使用暴露的第一个端口号)
      - traefik.http.services.my-service.loadbalancer.server.port=12345
```

2. 配置多个路由
``` yaml
version: "3"
services:
  my-container:
    # ...
    labels:
      # 路由1
      - traefik.http.routers.www-router.rule=Host(`example-a.com`)
      - traefik.http.routers.www-router.service=www-service
      - traefik.http.services.www-service.loadbalancer.server.port=8000

      # 路由2
      - traefik.http.routers.admin-router.rule=Host(`example-b.com`)
      - traefik.http.routers.admin-router.service=admin-service
      - traefik.http.services.admin-service.loadbalancer.server.port=9000 
```