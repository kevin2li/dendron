# 方法
使用python的`you-get`库

## 安装
```bash
pip install you-get
```

<!-- more -->

## 使用
### 直接下载
```bash
# 下载B站
you-get https://www.bilibili.com/video/BV1Ya411H7rV/?spm_id_from=333.999.0.0
```

### 使用代理

```powershell
$http_proxy="http://127.0.0.1:7890"
$https_proxy="http://127.0.0.1:7890"

# 下载youtube
you-get https://www.youtube.com/watch?v=oEORcCQ62nQ&ab_channel=DS6Inc
```