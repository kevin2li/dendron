# 简介

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1d9e8f9ec5a449c6d5f5d5e3b39914eb.image.png)

文档：https://doc.traefik.io/traefik/routing/providers/docker/

<!-- more -->

# 教程

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