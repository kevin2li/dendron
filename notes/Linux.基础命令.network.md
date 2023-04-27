---

id: 3hkev9qfedy3hp4194vs6qg
title: 网络管理
desc: ''
updated: 1682589185921
created: 1682484195294
---

### 基本网络配置
- `ping`


```bash
# Ping host:
ping host

# Ping a host only a specific number of times:
ping -c count host

# Ping host, specifying the interval in seconds between requests (default is 1 second):
ping -i seconds host

# Ping host without trying to lookup symbolic names for addresses:
ping -n host

# Ping host and ring the bell when a packet is received (if your terminal supports it):
ping -a host

# Also display a message if no response was received:
ping -O host
```
- `ifconfig`

```bash
# View network settings of an Ethernet adapter:
ifconfig eth0

# Display details of all interfaces, including disabled interfaces:
ifconfig -a

# Disable eth0 interface:
ifconfig eth0 down

# Enable eth0 interface:
ifconfig eth0 up

# Assign IP address to eth0 interface:
ifconfig eth0 ip_address
```
- `ip`

```bash
# List interfaces with detailed info:
ip address

# List interfaces with brief network layer info:
ip -brief address

# List interfaces with brief link layer info:
ip -brief link

# Display the routing table:
ip route

# Show neighbors (ARP table):
ip neighbour

# Make an interface up/down:
ip link set interface up/down

# Add/Delete an IP address to an interface:
ip addr add/del ip/mask dev interface

# Add a default route:
ip route add default via ip dev interface

```
- `route`

```bash
# Display the information of route table:
route -n

# Add route rule:
sudo route add -net ip_address netmask netmask_address gw gw_address

# Delete route rule:
sudo route del -net ip_address netmask netmask_address dev gw_address
```
- `traceroute`

```bash
# Traceroute to a host:
traceroute host

# Disable IP address and host name mapping:
traceroute -n host

# Specify wait time for response:
traceroute -w 0.5 host

# Specify number of queries per hop:
traceroute -q 5 host

# Specify size in bytes of probing packet:
traceroute host 42
```
- `lsof`

```bash
# Find the processes that have a given file open:
lsof path/to/file

# Find the process that opened a local internet port:
lsof -i :port

# Only output the process ID (PID):
lsof -t path/to/file

# List files opened by the given user:
lsof -u username

# List files opened by the given command or process:
lsof -c process_or_command_name

# List files opened by a specific process, given its PID:
lsof -p PID

# List open files in a directory:
lsof +D path/to/directory

# Find the process that is listening on a local IPv6 TCP port and don't convert network or port numbers:
lsof -i6TCP:port -sTCP:LISTEN -n -P
```
- `netstat`

```bash
# List all ports:
netstat --all

# List all listening ports:
netstat --listening

# List listening TCP ports:
netstat --tcp

# Display PID and program names:
netstat --program

# List information continuously:
netstat --continuous

# List routes and do not resolve IP addresses to hostnames:
netstat --route --numeric

# List listening TCP and UDP ports (+ user and process if you're root):
netstat --listening --program --numeric --tcp --udp --extend
```
### 防火墙
- `firewall-cmd`

```bash
# View the available firewall zones:
firewall-cmd --get-active-zones

# View the rules which are currently applied:
firewall-cmd --list-all

# Permanently move the interface into the block zone, effectively blocking all communication:
firewall-cmd --permanent --zone=block --change-interface=enp1s0

# Permanently open the port for a service in the specified zone (like port 443 when in the `public` zone):
firewall-cmd --permanent --zone=public --add-service=https

# Permanently close the port for a service in the specified zone (like port 80 when in the `public` zone):
firewall-cmd --permanent --zone=public --remove-service=http

# Permanently open two arbitrary ports in the specified zone:
firewall-cmd --permanent --zone=public --add-port=25565/tcp --add-port=19132/udp

# Reload firewalld to force rule changes to take effect:
firewall-cmd --reload
```
- `iptables`

```bash
# View chains, rules, and packet/byte counters for the filter table:
sudo iptables -vnL

# Set chain policy rule:
sudo iptables -P chain rule

# Append rule to chain policy for IP:
sudo iptables -A chain -s ip -j rule

# Append rule to chain policy for IP considering protocol and port:
sudo iptables -A chain -s ip -p protocol --dport port -j rule

# Add a NAT rule to translate all traffic from the `192.168.0.0/24` subnet to the host's public IP:
sudo iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j MASQUERADE

# Delete chain rule:
sudo iptables -D chain rule_line_number

# Save iptables configuration of a given table to a file:
sudo iptables-save -t tablename > path/to/iptables_file

# Restore iptables configuration from a file:
sudo iptables-restore < path/to/iptables_file
```
### 抓包
- `tcpdump`

```bash
# List available network interfaces:
tcpdump -D

# Capture the traffic of a specific interface:
tcpdump -i eth0

# Capture all TCP traffic showing contents (ASCII) in console:
tcpdump -A tcp

# Capture the traffic from or to a host:
tcpdump host www.example.com

# Capture the traffic from a specific interface, source, destination and destination port:
tcpdump -i eth0 src 192.168.1.1 and dst 192.168.1.2 and dst port 80

# Capture the traffic of a network:
tcpdump net 192.168.1.0/24

# Capture all traffic except traffic over port 22 and save to a dump file:
tcpdump -w dumpfile.pcap port not 22

# Read from a given dump file:
tcpdump -r dumpfile.pcap
```
- `tshark`

### 扫描
- `nmap`
```bash
# 安装
sudo apt install nmap

# 端口扫描
sudo nmap -Pn 192.168.2.121
nmap -sV -p 1-65535 192.168.1.1/24
```

- `ncat`
```bash
# Connect to example.org on TCP port 8080.
ncat example.org 8080

# Listen for connections on TCP port 8080.
ncat -l 8080

# Redirect TCP port 8080 on the local machine to host on port 80.
ncat --sh-exec "ncat example.org 80" -l 8080 --keep-open

# Bind to TCP port 8081 and attach /bin/bash for the world to access freely.
ncat --exec "/bin/bash" -l 8081 --keep-open

# Bind a shell to TCP port 8081, limit access to hosts on a local network, and limit the maximum number of simultaneous connections to 3.
ncat --exec "/bin/bash" --max-conns 3 --allow 192.168.0.0/24 -l 8081 --keep-open

# Connect to smtphost:25 through a SOCKS4 server on port 1080.
ncat --proxy socks4host --proxy-type socks4 --proxy-auth joe smtphost 25

# Connect to smtphost:25 through a SOCKS5 server on port 1080.
ncat --proxy socks5host --proxy-type socks5 --proxy-auth joe:secret smtphost 25

# Create an HTTP proxy server on localhost port 8888.
ncat -l --proxy-type http localhost 8888

# Send a file over TCP port 9899 from host2 (client) to host1 (server).
HOST1$ ncat -l 9899 > outputfile

HOST2$ ncat HOST1 9899 < inputfile

# Transfer in the other direction, turning Ncat into a “one file” server.
HOST1$ ncat -l 9899 < inputfile
HOST2$ ncat HOST1 9899 > outputfile
```
- `nc`

```bash
# Open a TCP connection to port 42 of host.example.com, using port 31337 as the source port, with a timeout of 5 seconds:
nc -p 31337 -w 5 host.example.com 42

# Open a UDP connection to port 53 of host.example.com:
nc -u host.example.com 53

# Open a TCP connection to port 42 of host.example.com using 10.1.2.3 as the IP for the local end of the connection:
nc -s 10.1.2.3 host.example.com 42

# Create and listen on a UNIX-domain stream socket:
nc -lU /var/tmp/dsocket

# Connect to port 42 of host.example.com via an HTTP proxy at 10.2.3.4, port 8080.  This example could also be used by ssh(1); see the ProxyCommand directive in ssh_config(5) for more information.
nc -x10.2.3.4:8080 -Xconnect host.example.com 42

# The same example again, this time enabling proxy authentication with username “ruser” if the proxy requires it:
nc -x10.2.3.4:8080 -Xconnect -Pruser host.example.com 42
```
### 下载
- `wget`
- `curl`

```bash
# 携带数据
curl -d "name=curl" https://example.com
curl -d "name=curl" -d "tool=cmdline" https://example.com

# 表单数据(Content-Type multipart/form-data)
curl -F name=John -F shoesize=11 https://example.com/
curl -F profile=@portrait.jpg https://example.com/upload.cgi
 
# POST请求
curl -d '{"channel":"4","ifautologin":"0","pagesign":"secondauth"}' -H "Content-Type: application/json" -X POST http://10.255.255.34/api/v1/login

# 下载保存
curl -o output.html http://example.com/
curl -O http://example.com/file.html

# 自动重定向
curl -L https://example.com

# 使用代理
curl -x socks5://192.168.2.1:10080 https://www.baidu.com
curl -x http://user:password@proxy.example.com:8080 http://www.example.com
curl -U daniel:secr3t -x myproxy:80 http://example.com
curl --proxy-header "User-Agent: magic/3000" -x proxy https://example.com/
```
- `axel`

```bash
# Download a URL to a file:
axel url

# Download and specify filename:
axel url -o path/to/file

# Download with multiple connections:
axel -n connections_num url

# Search for mirrors:
axel -S mirrors_num url

# Limit download speed (bytes per second):
axel -s speed url
```
### 监控流量
- `iftop`
```bash
# Show the bandwidth usage:
sudo iftop

# Show the bandwidth usage of a given interface:
sudo iftop -i interface

# Show the bandwidth usage with port information:
sudo iftop -P

# Do not show bar graphs of traffic:
sudo iftop -b

# Do not look up hostnames:
sudo iftop -n
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c3347f697509e1a47e9cb8159b831999.image.png)