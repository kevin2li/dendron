---
id: eze35xs00yuwxd6dun42j3x
title: Linux根据pid查找进程具体目录
desc: ''
updated: 1684905800793
created: 1684892153074
---
## 查找pid

- 根据监听端口号查找：
``` bash 
sudo netstat -tlnp
```
![](https://minio.kevin2li.top/image-bed/blog/20230524131750.png)

- 根据占用端口号查找

``` bash 
sudo lsof -i:8080
```
![](https://minio.kevin2li.top/image-bed/blog/20230524131900.png)

- 根据进程名称查找
``` bash 
ps -ef | grep ssh
```

![](https://minio.kevin2li.top/image-bed/blog/20230524132300.png)

## 方法
假设你通过前面步骤找到了你感兴趣的进程pid号，你可以进一步的查看具体的进程目录和可执行程序路径。
```bash
cd /proc/<pid>
ls -la
```
如图所示，  
- `cwd`: 进程的工作目录  
- `exe`: 进程的二进制文件路径 

![](https://minio.kevin2li.top/image-bed/blog/20230524092339.png)

但是现在只能看到执行的命令，看不到命令执行携带的参数，可以通过下面命令进一步查看：
``` bash
# 查询单个pid
ps -p {pid} -o pid,cmd

# 查询多个pid
ps -p {pid1,pid2} -o pid,cmd
```

![](https://minio.kevin2li.top/image-bed/blog/20230524093401.png)