# 简介
GraphInsight是一款优秀的图分析工具，支持用户上传本地图数据或连接图数据库进行数据探索分析，挖掘数据特征，支持各种数据规模下的图关联分析，功能丰富，包含大量实用的资产，用户可按需组合选择所需资产进行针对性的分析。本教程将介绍如何安装GraphInsight，以及连接图数据库TuGraph。

![20221209222008.png](https://minio.kevin2li.top/image-bed/vanblog/img/e1d908dcdfad59c1bb11a09779625288.20221209222008.png)

本教程将会安装如下3个应用；
- GraphInsight：图可视化分析工具
- TuGraph：图数据库
- GraphVis： GraphInsight连接TuGraph依赖的http server

<!-- more -->

# 安装
## TuGraph
官网：https://www.tugraph.org/  
文档：https://www.tugraph.org/doc  
TuGraph有多种安装方式，本教程只介绍docker版的安装方式，二进制安装可参考文档。
```bash
mkdir tugraph
vim docker-compose.yaml
```
`docker-compose.yaml`内容如下：
```yaml
version: '3.9'
services:
    tugraph:
        container_name: tugraph
        image: tugraph/tugraph-db-centos7:3.3.0
        hostname: tugraph-host
        ports:
          - "8080:7070"
          - "10000:9090"
        volumes:
          - "./lgraph_db:/var/lib/lgraph/data"
        command: "lgraph_server"
        restart: 'unless-stopped'
```
启动：`docker compose up -d`  
此时，可访问`http://localhost:8080`查看TuGraph的web首页。  

![](https://minio.kevin2li.top/image-bed/vanblog/img/17ed8175a8283dcb29bacda6b718d85a.20221209214028.png)

:::tip{title="初始账号密码"}
用户名: admin
密码： 73@TuGraph
:::

## GraphVis
参考： https://www.yuque.com/antv/gi/wuvtyf#aO609
```bash
# 1.拉取镜像
docker pull antvis/graph_vis_service:1.1.0
# 2.启动镜像
docker run -d -p 7001:7001 -it --name antvis --rm antvis/graph_vis_service:1.1.0
# 3.进入容器启动服务
docker exec -it graphvis bash
npm run dev -p 7001 # 容器内执行
```

## GraphInsight
Github: https://github.com/antvis/GraphInsight  
文档: https://www.yuque.com/antv/gi/wuvtyf#aO609  

安装步骤如下：
```bash
# 1.克隆仓库
git clone git@github.com:antvis/GraphInsight.git
# 2.切入项目目录
cd GraphInsight
# 3.安装依赖
pnpm install
# 4.启动
npm run start 
```
此时，可访问`http://localhost:8000`查看GraphInsight的web首页。 

![](https://minio.kevin2li.top/image-bed/vanblog/img/880e135e20286c7558e21a182f1e38e8.20221209220512.png)

:::info{title="连接TuGraph"}
在图数据源中选择TuGraph，并依次设置数据库连接地址和账号密码，连接成功后再选择子图，此时页面会重启。  

![](https://minio.kevin2li.top/image-bed/vanblog/img/3d11e54ea0c2fc08d94868c0c08b838f.20221209221415.png)

在重启后的页面上是没有数据的，需要选择Cypher资产组件，使用cypher语句查询数据后渲染到画布上。  

![](https://minio.kevin2li.top/image-bed/vanblog/img/8b27d4d9ce636170056f5b38f0929ca8.20221209221746.png)
:::