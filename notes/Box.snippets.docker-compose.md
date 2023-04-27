---
id: 2qk9bp379ihkcjmi9xcxac9
title: docker-compose
desc: ''
updated: 1682560644022
created: 1682559590262
---

[docker-compose文档](https://docs.docker.com/compose/compose-file/05-services/)

``` yaml
version: "3.9"

services:
  srv_name:
    image: awesome/backend
    container_name: srv_name
    restart: unless-stopped # always
    
    # 环境变量设置
    environment:
      TZ: "Asia/Shanghai"

    # env_file: ./docker.env

    # 数据卷设置
    volumes:
      - ${PWD}/data:/app/data
      - database-data:/app/data2

    # 网络设置 
    networks:
      - internal
    # network_mode: "host"
    
    # 端口映射
    ports:
      - 9001:6412

    # 执行命令
    # command: ["redis-server", "/redis.conf"]

    # 依赖顺序
    # depends_on:
    #   - redis

networks:
  internal:
    driver: bridge
    name: vanblog-network
  nginx:
    external: true

volumes:
  database-data:
```