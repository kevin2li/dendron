---
id: x9zf7smyqcligvln1rq5wfk
title: 磁盘管理
desc: ''
updated: 1682562381146
created: 1682484188721
---


## 磁盘管理
- `fdisk`
```bash
# List partitions:
sudo fdisk -l

# Start the partition manipulator:
sudo fdisk /dev/sdX

# Once partitioning a disk, create a partition:
n

# Once partitioning a disk, select a partition to delete:
d

# Once partitioning a disk, view the partition table:
p

# Once partitioning a disk, write the changes made:
w

# Once partitioning a disk, discard the changes made:
q

# Once partitioning a disk, open a help menu:
m
```

- `mount`

```bash
# 将设备 "/dev/sdb1" 挂载到 "/mnt/media" 目录
sudo mount /dev/sdb1 /mnt/media
```
:::info{title="相关信息"}
格式：
`mount [OPTION...] DEVICE_NAME DIRECTORY`
:::

- `umount`
```bash
umount DIRECTORY
umount DEVICE_NAME
```
- `df`
```bash
# Display all filesystems and their disk usage:
df

# Display all filesystems and their disk usage in human-readable form:
df -h

# Display the filesystem and its disk usage containing the given file or directory:
df path/to/file_or_directory

# Display statistics on the number of free inodes:
df -i

# Display filesystems but exclude the specified types:
df -x squashfs -x tmpfs
```
- `du`
```bash
# List the sizes of a directory and any subdirectories, in the given unit (B/KiB/MiB):
du -b|k|m path/to/directory

# List the sizes of a directory and any subdirectories, in human-readable form (i.e. auto-selecting the appropriate unit for each size):
du -h path/to/directory

# Show the size of a single directory, in human-readable units:
du -sh path/to/directory

# List the human-readable sizes of a directory and of all the files and directories within it:
du -ah path/to/directory

# List the human-readable sizes of a directory and any subdirectories, up to N levels deep:
du -h --max-depth=N path/to/directory

# List the human-readable size of all `.jpg` files in subdirectories of the current directory, and show a cumulative total at the end:
du -ch */*.jpg
```
- `lsblk`  
列出块设备,可以查看到块设备的挂载点

```bash
# List all storage devices in a tree-like format:
lsblk

# Also list empty devices:
lsblk -a

# Print the SIZE column in bytes rather than in a human-readable format:
lsblk -b

# Output info about filesystems:
lsblk -f

# Use ASCII characters for tree formatting:
lsblk -i

# Output info about block-device topology:
lsblk -t

# Exclude the devices specified by the comma-separated list of major device numbers:
lsblk -e 1,7

# Display a customized summary using a comma-separated list of columns:
lsblk --output NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT
```

![image.png](https://kevin2li.top/static/img/a782557c2deceee5720cf743b319a1c3.image.png)
- `lsusb`  

```bash
# List all the USB devices available:
lsusb

# List the USB hierarchy as a tree:
lsusb -t

# List verbose information about USB devices:
lsusb --verbose

# List detailed information about a USB device:
lsusb -D {{device}}

# List devices with a specified vendor and product ID only:
lsusb -d {{vendor}}:{{product}}
```
- `lspci`  

```bash
# Show a brief list of devices:
lspci

# Display additional info:
lspci -v

# Display drivers and modules handling each device:
lspci -k

# Show a specific device:
lspci -s {{00:18.3}}

# Dump info in a readable form:
lspci -vm
```
- `iotop`  
```bash
# 查看所有进程的磁盘I/O
sudo iotop

# 查看当前实际进行磁盘I/O的进程
sudo iotop -o

# 查看指定进程的磁盘I/O情况
sudo iotop -p 22
```
输出：

![image.png](https://kevin2li.top/static/img/db000798190b020829a6a243333aac05.image.png)