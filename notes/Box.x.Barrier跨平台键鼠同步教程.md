---
id: ssc4q3zftrz63t3yiklvi6y
title: Barrier跨平台键鼠同步教程
desc: ''
updated: 1691849906623
created: 1691844838203
---

## Windows

> 参考：https://github.com/debauchee/barrier/issues/1952

1. 下载openssl.cnf

下载文件：
`https://github.com/debauchee/barrier/blob/master/ext/openssl/windows/x64/ssl/openssl.cnf`

拷贝到：
`C:\OpenSSL\ssl\openssl.cnf`

2. ssl生成

```powershell
& 'C:\Program Files\Barrier\openssl.exe' req -x509 -nodes -days 365 -subj /CN=Barrier -newkey rsa:4096 -keyout "C:\Users\<user>\AppData\Local\Barrier\SSL\Barrier.pem" -out "C:\Users\<user>\AppData\Local\Barrier\SSL\Barrier.pem"

```

## MacOS
>参考： https://github.com/debauchee/barrier/issues/1609
```bash
cd "/Users/<user>/Library/Application Support/barrier/SSL"
openssl req -new -x509 -sha256 -days 999 -nodes -out Barrier.pem -keyout Barrier.pem
```

## FAQ
1. win键鼠控制mac，鼠标不显示  

https://github.com/debauchee/barrier/issues/42