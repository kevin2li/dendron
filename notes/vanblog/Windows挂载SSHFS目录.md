# 简介
参考：https://github.com/winfsp/sshfs-win


<!-- more -->

# 方法
## 安装

```powershell
winget install WinFsp.WinFsp; winget install SSHFS-Win.SSHFS-Win
```
## 挂载

```powershell
net use X: \\sshfs\billziss@mac2018.local
```

## 查看挂载列表
```powershell
net use
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/054a9534ff9776a15d1392bb1a8b4519.image.png)

## 取消挂载
```powershell
net use X: /delete
```