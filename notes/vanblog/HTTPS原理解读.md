# 简介


<!-- more -->

# 基础知识
## 密码学
### 单向加密
由明文生成密文简单，由密文恢复明文非常困难。

#### 特点
1. 不可逆
2. 数据敏感，输入不同输出不同(除非发生哈希碰撞)

#### 常用算法
MD5、sha256等

#### 应用场景
1. 数据完整性校验：检验数据是否被篡改

>如`Miniconda3`使用SHA256哈希摘要来验证数据完整性。
>
>![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d2ec6a4bd0f15da5de940c175dd738b0.image.png)
>
>地址：https://docs.conda.io/en/latest/miniconda.html

检验代码：
```python
import hashlib

def digest(path, algorighm="sha256"):
    if algorighm == "sha256":
        m = hashlib.sha256()
    elif algorighm == "md5":
        m = hashlib.md5()
    else:
        raise ValueError("Unsupport hash algorithm!")
    with open(path, "rb") as f:
        data = f.read()
    m.update(data)
    return m.hexdigest()

# 计算
path = "Miniconda3-latest-Linux-x86_64.sh"
digest(path)
```
2. 数据库密码存储：将其加密后再存储而不是直接存储明文

### 对称加密
加密和解密使用同一个密钥

#### 常用算法
DES、3DES、AES等

#### 特点
1. 加解效率较高
2. 加解密使用同一密钥

#### 应用场景
用于对效率有要求的实时数据加密通信。比如在使用VPN或者代理进行加密通信时

### 非对称加密

#### 特点
1. 加解密效率较低
2. 使用两个密钥且成对出现，公钥加密可以用私钥解密，私钥加密可以公钥解密

#### 常用算法
RSA、DSA等

#### 应用场景
主要用于秘钥交换、证书等场景


:::info{title="公/私钥加密的使用场景"}
1. **公钥加密可保证只有对应私钥持有者能查看**  
当我有数据只希望你能看到，不希望被其他人破解，可以用你的公钥加密数据，这样就只有你用你的私钥才能解密查看。

2. **私钥加密可用作数字签名**  
当我需要证明数据是经过我确认的时候，可以用我的私钥对数据进行加密得到签名，他人可以用我的公钥解密进行验证。
:::


## 证书认证中心(CA)
在使用非对称加密传输数据时，可能会发生中间人攻击。 CA的作用可以保证公钥安全传输到客户端。


# HTTPS协议
思路：
1. 原先的HTTP协议客户端和服务器之间是明文传输的，不够安全，为了提高安全性需要对内容进行加密。

2. 加密算法选择  
    - 单向加密不能恢复明文，不可取
    - 非对称加解密效率太低，而http 的应用场景中通常端与端之间存在大量的交互，非对称加密的效率是无法接受的，故而不可取
    - 对称加密效率较高，但仍存在一些问题，可以在其基础上改进

3. 对称加密的问题  
一旦密钥泄漏，就没有秘密可言了。即使对密钥再进行对称加密还是有泄漏风险。

4. 使用非对称加密协商对称加密的密钥  
客户端使用服务器的公钥对密钥加密，即使密文被拦截也破解不了，只有服务器持有对应的私钥能解开。  

新的问题出现了：如何保证客户端拿到的公钥就是服务器的公钥，可能会被中间人攻击。如本地请求被劫持（如 DNS 劫持等），所有请求均发送到中间人的服务器。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/3c2fcff042981ff018ba5ebb24da5b5c.image.png)

6. 保证公钥安全传输  
客户端选择相信CA机构，客户端也内置了很多CA机构的证书，访问服务器时也会先验证服务器证书的合法性，只有通过CA机构颁发的证书才可以进行下一步数据传输。

证书里包含如下等信息：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c2c7557f53b3f238fc7323f0ec2913e7.image.png)

服务器去CA机构申请数字证书，CA机构会验证服务器公钥的合法性，验证通过后颁发数字证书，里面含有CA机构的签名，该签名只能由CA机构的私钥加密生成，中间人无法破解，从而避免了中间人攻击。

7. 保证数据不被篡改  
对传输的数据进行哈希计算得到摘要，用自己的私钥对摘要进行签名。当别人对数据进行篡改时，由于没有原服务器的私钥，无法进行签名，即使篡改者用自己的私钥签名，在客户端验证时是使用原服务器的公钥验证因此肯定不通过，从而被发现篡改。

## SSL/TLS协议
https相当于在http+tls。
TLS协议位于协议栈中的会话层。

> 参考：https://www.oreilly.com/library/view/high-performance-browser/9781449344757/ch04.html

![](https://minio.kevin2li.top/image-bed/blog/20230601180024.png)


TLS Handshake过程：

![](https://minio.kevin2li.top/image-bed/blog/20230601175955.png)


TLS Record格式：

![](https://minio.kevin2li.top/image-bed/blog/20230601180055.png)

## 实战分析
思路：先在Linux机器上通过`curl`命令发起网络请求，并用`tcpdump`捕获期间产生的网络包，然后导入到wireshark中进行分析。
> 参考：https://everything.curl.dev/usingcurl/tls/sslkeylogfile

1. 准备抓包
```bash
sudo tcpdump -nn host blog.kevin2li.top and port 443 -w blog.pcap
```
3. 发起https网络请求
```bash
# 设置`SSLKEYLOGFILE`环境变量
export SSLKEYLOGFILE="$PWD/keylog.log"

# 发起https网络请求
curl https://blog.kevin2li.top
```
3. 导入wireshark分析  
1)设置pre master secret.

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/201ceda00181410aeafa34804785c9c7.image.png)

2)打开`blog.pcap`。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/7cc8e6a145d8d1ac2ee752ba0fdfb7ff.image.png)

`Client Hello`:

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/da63cd64a994488153c6eae8d5af60b7.image.png)

流量图分析：
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ab98880a8b615435019f0415167ed069.image.png)

# 参考
1. [OSC开源社区-通俗大白话，彻底弄懂https原理本质 ](https://mp.weixin.qq.com/s?__biz=MjM5NzM0MjcyMQ==&mid=2650164959&idx=4&sn=99796a4661f87592ea33bbe5589d766e&chksm=bed995b189ae1ca7191c9f2eea9cfe52ffa8b33037010ed14ff9bb747cd99b86a46af62466ab&mpshare=1&scene=1&srcid=04203iwg7CXVr0E3Fb1t2hf9&sharer_sharetime=1681976234165&sharer_shareid=b44ebbe82718b61b6a9fa0be4bb87fab#rd)
