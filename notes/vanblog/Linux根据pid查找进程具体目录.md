# 方法
假设你通过`top`、`ps`等命令找到了你感兴趣的进程pid号，你可以进一步的查看具体的进程目录和可执行程序路径。
```bash
cd /proc/<pid>
ls -la
```
如图所示，  
`cwd`: 进程的工作目录  
`exe`: 进程的二进制文件路径 

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4e3a28d3b5c8d86c804f09dda135b2e4.image.png)


<!-- more -->
