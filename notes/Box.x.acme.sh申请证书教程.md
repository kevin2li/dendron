---
id: lxo6k7lxup7j1hrjycu8ok3
title: sh申请证书教程
desc: ''
updated: 1684302122992
created: 1684285703425
---

## 步骤
- 创建dns密钥  
https://console.dnspod.cn/account/token/token
![](https://kevin2li-storage.oss-cn-nanjing.aliyuncs.com/image/2022-10-10-15-54-57.png)

- acme设置
```bash
# 安装acme
curl  https://get.acme.sh | sh 
cd ~/.acme.sh

# 注册账号
./acme.sh --register-account -m kevin2li@qq.com

# 配置密钥
export DP_Id="id"
export DP_Key="token"

# 生成证书
./acme.sh --issue --dns dns_dp -d kevin2li.top -d "*.kevin2li.top"
```
- 安装证书
![](https://kevin2li-storage.oss-cn-nanjing.aliyuncs.com/image/2022-10-10-15-58-07.png)
fullchain.cer为证书文件，kevin2li.top.key为密钥文件,使用nginx配置ssl即可

建议：不要直接使用上面的文件，可以将其复制到其他目录再使用，如nginx下可以复制到`/etc/nginx/ssl/`目录下

**nginx:**
```bash
# 拷贝证书
mkdir -p /etc/nginx/ssl/kevin2li.top
cp ~/.acme.sh/kevin2li.top/fullchain.cer ~/.acme.sh/kevin2li.top/kevin2li.top.key /etc/nginx/ssl/kevin2li.top/

# 安装证书
acme.sh --installcert -d kevin2li.top --key-file /etc/nginx/ssl/kevin2li.top.key --fullchain-file /etc/nginx/ssl/kevin2li.top.fullchain.cer --reloadcmd  "service nginx force-reload"
```
安装成功后会自动注册一个定时任务来检测证书并适时更新证书。
![](https://minio.kevin2li.top/image-bed/202305171340159.png)