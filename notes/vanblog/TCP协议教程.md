# 抓包工具
## tcpdump
命令格式：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/88362912bab78d3461107e1ac1594822.image.png)

常用参数：
- `-i`：指定网卡接口，`-i any`可以使用所有接口
- `-c`: 指定抓包数量
- `-nn`: 不解析主机地址和端口号为名字
- `-S`: 打印绝对TCP序列号，而不是相对序列号
- `-X`: 以以hex和ASCII形式打印数据包内容
- `-w`: 将结果写入文件，通常后缀为`.pcap`
- `-D`: 查看拥有的网络接口

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/09bb19cf68d7756dda62960a1946fa0a.image.png)

<!-- more -->

表达式语法：

> 参考：[肝了三天，万字长文教你玩转 tcpdump，从此抓包不用愁](https://mp.weixin.qq.com/s?__biz=Mzg3MjU3NzU1OA==&mid=2247496415&idx=1&sn=cb549cd19397881dd7035f234c36fc33&chksm=ceef9da6f99814b0d6c8bcf60ed161cb01fd03b11a42be7653e51a6d77b027b7cedfb29c6137&mpshare=1&scene=1&srcid=0912qdDeHqFWxYSm3qav86RI&sharer_sharetime=1662960495870&sharer_shareid=b44ebbe82718b61b6a9fa0be4bb87fab#rd)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/435c38a6e33ddfa17d6f629be7a6847b.image.png)

抓包结果格式：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2e50d419dbace6b9a615b175c06dfe92.image.png)


TCP标志位介绍：  
- `[S]` : SYN（开始连接）

- `[P]` : PSH（推送数据）

- `[F]` : FIN （结束连接）

- `[R]` : RST（重置连接）

- `[.]` : 没有 Flag，由于除了 SYN 包外所有的数据包都有ACK，所以一般这个标志也可表示 ACK

**使用举例：**

- 根据主机IP过滤

```bash
tcpdump host 192.168.10.100
tcpdump src host 192.168.10.100
tcpdump dst host 192.168.10.200
```

- 根据网段过滤
```bash
tcpdump net 192.168.10.0/24
tcpdump src net 192.168.10.0/24
tcpdump dst net 192.168.10.0/24
```
- 根据端口过滤

```bash
# 单一端口
tcpdump port 8088
tcpdump src port 8088
tcpdump dst port 8088

# 端口范围
tcpdump portrange 8000-8080
tcpdump src portrange 8000-8080
tcpdump dst portrange 8000-8080
```
- 根据协议过滤

```bash
tcpdump icmp
tcpdump 'ip proto tcp'
tcpdump 'ip6 proto tcp'
```
- 组合过滤

:::info{title="相关信息"}
1. 逻辑语句：`and`, `or`, `not` 或 `&&`, `||`, `!`

2. 判断语句：`=`, `==`, `!=`

内置变量：  
- `if`: 网卡接口名  
- `proc`: 进程名  
- `pid`: 进程id  
- `dir`: 方向  

```bash
# 过滤来自进程名为 nc 发出的流经 en0 网卡的数据包，或者不流经 en0 的入方向数据包
tcpdump "( if=en0 and proc=nc ) || (if != en0 and dir=in)"
```
:::

```bash
# find all traffic from 10.5.2.3 going to any host on port 3389
tcpdump -nnvvS src 10.5.2.3 and dst port 3389

# look for all traffic coming from 192.168.x.x and going to the 10.x or 172.16.x.x networks
tcpdump -nvX src net 192.168.0.0/16 and dst net 10.0.0.0/8 or 172.16.0.0/16

# look for all traffic going to 192.168.0.2 that is not ICMP
tcpdump dst 192.168.0.2 and src net and not icmp

# look for all traffic from a host that isn’t SSH traffic
tcpdump -vv src mars and not dst port 22

tcpdump 'src 10.0.2.4 and (dst port 3389 or 22)'
```
- 根据标志位过滤

```bash
# 指定标志位
tcpdump 'tcp[13] & 2!=0'
tcpdump 'tcp[tcpflags] == tcp-syn'
```

## Wireshark

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/569487695f17b27574e451195f071e11.image.png)

**1. 捕获过滤表达式：**  
语法与`tcpdump`类似。先设定条件再进行抓包。

**2. 显示过滤表达式：**  
在抓完包后根据设定条件筛选感兴趣的包。

- 根据ip过滤

```bash
ip.src == 192.168.0.1
ip.dst == 192.168.0.1
ip.addr == 192.168.0.1
!(ip.addr == 192.168.0.1)
```
- 根据网段过滤

```bash

```
- 根据端口过滤
```bash
tcp.port == 80
udp.port >= 2048
```
- 根据协议过滤

```bash
http
http or telnet
not arp # 或!arp

# 根据标志位过滤
tcp.flags.syn==1
tcp/flags.rst==1
```

- 根据长度过滤
```bash
udp.length < 20   
http.content_length <=30
```
- 根据内容过滤
 
```bash
http.request.uri matches "user" 
http.request.uri contains "User"
http.host==baidu.com
http.host contains "baidu"
http.content_type =="text/html"
http.request.method=="POST"
http.response.code==302
http.cookie contains "userid"
```
- 组合过滤

```bash
ip.addr==192.168.2.121 && tcp.port==10080
```
:::tip{title="显示绝对序列号"}

`编辑>首选项>Protocols>TCP`  

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/69aa123857090b17ea8e40d9ccda1b51.image.png)
:::


:::tip{title="抓https网络包"}
参考：https://www.comparitech.com/net-admin/decrypt-ssl-with-wireshark/
1. 设置系统环境变量`SSLKEYLOGFILE`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/de1aa7f50fc53f27511095a2204b25aa.image.png)

2. 设置Wireshark的pre master secret。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1e174aa2718e74c62702d7ad7fbb193a.image.png)

3. 使用浏览器访问https网站  
注意：目前火狐浏览器和Chrome浏览器支持，其他浏览器不一定支持。

5. 抓包

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/79b9183ee45494f84204fb25b6e9c5d0.image.png)

:::
# TCP协议格式

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/739ff0bf9f06e941369bbe3cc3a8934f.image.png)

**字段说明**：
- `源端口`：2字节。
- `目的端口`: 2字节。
- `序号`: 本报文段所发送的数据的第一个字节的序号。`下一个报文段的序号=当前报文段序号+当前报文段数据长度`。
- `确认号`: 期望收到对方下一个报文段的第一个数据节的序号。
`确认号=接收报文段序号+接收报文段数据长度`。
- `数据偏移`：反映了TCP报文段的首部长度，含义为数据起始位置相对于TCP报文起始位置的距离。单位为4字节，说明报文首部长度最大为15*4=60字节。
- `保留`: 6位，暂时不用，置为零。
- `控制位`:
    - `URG`: 紧急位，告诉系统此报文段含有紧急数据需尽快传送，而不要按原来排队顺序传送。配合后面`紧急指针`一起使用。
    - `ACK`：确认位，在连接建立后所有传送的报文段都必须把 ACK 置 1。
    - `PSH`: 推送位，当该位置1时，发送方立即发送，接收方立即向上交付，而不再等缓存填满再交付。
    - `RST`: 重置位，表明TCP连接出现严重差错，需要释放连接重新建立。
    - `SYN`: 同步位，在建立连接时用来同步序号。
    - `FIN`: 终止位，在关闭连接时用到。
- `窗口`: 接收窗口大小，告诉发送方自己目前允许对方发送的数据量，单位为字节，经常动态变化。
- `检验和`: 检验范围包括首部和数据两部分。
- `紧急指针`: 指出本报文段紧急数据的字节数，紧急数据后为普通数据。
- `选项`: 长度可变，最大为40字节。


# IP协议格式

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4d4132b0beb25a3a27226660db91c937.image.png)

**字段说明**：
- `版本`：IP协议版本。
- `首部长度`: 占4位，可表示数据范围为0~15，单位为4字节，表明首部长度最大为15*4=60字节。
- `区分服务`: 暂时不用。
- `总长度`: 首部和数据之和的长度。最大为65535字节。实际上不能超过MTU(以太网规定MTU为1500字节)，否则会进行分片。
- `标识`: 数据报的编号，当产生分片时，利用该字段便于将属于同一数据包的各个分片重新组装。
- `标志`: 标志位，占3位，只用到2位：
    - `MF`: `MF=1`表示后面还有分片。
    - `DF`: `DF=1`表示不能分片，只有为0时才允许分片。
- `片偏移`: 指出该分片在原始分组数据字段的起点的相对偏移位置，单位为8字节。
- `生存时间`: `TTL`(Time To Live)，至多允许的跳数。
- `协议`: 数据字段部分使用的协议。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/132f33c3f97fed92a874c5f018083977.image.png)

- `首部检验和`: 只检验首部，不包括数据部分。
- `源地址`: 4字节
- `目标地址`：4字节

# 实战分析

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6c9444675ce0d35d5e97b283bf9e33b3.image.png)

1. 在机器B上搭建一个http服务

```bash
python -m http.server 9099
```
2. 在机器A上使用tcpdump准备抓包

```bash
sudo tcpdump -nnS -i wlx90de8095c21f host 192.168.2.121 and port 9099 -w test.pcap
```
4. 在机器A上访问机器B上的http服务
```bash
curl http://192.168.2.121:9099
```
3. 将抓到的包文件`test.cap`导入wireshark分析

流量图分析：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1494605f76e3535f517d697f78b64441.image.png)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/634d89585bfa16c03eec0fefbd0b8ecd.image.png)

可以看到，前三个包是建立tcp连接的过程，最后两个包是关闭tcp连接的过程。

# 参考
1. [java3y-实战-图解TCP](https://mp.weixin.qq.com/s?__biz=MzI4Njg5MDA5NA==&mid=2247490413&idx=3&sn=0781cc043cdf46990e1fe7f49ef175d8&chksm=ebd75a6cdca0d37a12cf8239c7701d562aaf9b2bf6a77a5769df8def2ef6233bcd0bbd5708cf&mpshare=1&scene=1&srcid=0420lU6NUxp6kvWCBheOci0A&sharer_sharetime=1681952381109&sharer_shareid=b44ebbe82718b61b6a9fa0be4bb87fab#rd)