---
id: aa8le8atvsf3m0vkk19ystp
title: ProxmoxVE核显直通
desc: ''
updated: 1685271331456
created: 1685263057557
---

## 简介
参考：
1. https://pve.proxmox.com/wiki/PCI_Passthrough
2. [知乎 |【NAS】PVE的简单使用教程、调优、常见问题汇总](https://zhuanlan.zhihu.com/p/614820460?utm_campaign=shareopn&utm_medium=social&utm_oi=790165242284998656&utm_psn=1646204336614219777&utm_source=wechat_session)

## 方法
1. 修改`/etc/default/grub`

(可能本来就有)
``` bash 
# 将 GRUB_CMDLINE_LINUX_DEFAULT="quiet"
# 替换为：
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt video=vesafb:off video=efifb:off"
```

重启后，验证：
``` bash 
dmesg | grep -e DMAR -e IOMMU
```

![](https://minio.kevin2li.top/image-bed/blog/20230528164131.png)

2. 修改`/etc/modules`  

添加以下内容(部分可能本来就有)

``` bash 
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```
3. 修改`/etc/modprobe.d/blacklist.conf`  

添加驱动黑名单(根据自己显卡类型选择)

``` bash 
# block AMD driver
blacklist radeon
blacklist amdgpu
​
# block NVIDIA driver
blacklist nouveau
blacklist nvidia
blacklist nvidiafb
​
# block INTEL driver
blacklist snd_hda_intel
blacklist snd_hda_codec_hdmi
blacklist i915
```

4. 检查IOMMU中断映射(IOMMU Interrupt Remapping)
``` bash 
dmesg | grep 'remapping'
```

![](https://minio.kevin2li.top/image-bed/blog/20230528165403.png)

出现下面之一，视为正常：
- "AMD-Vi: Interrupt remapping enabled"
- "DMAR-IR: Enabled IRQ remapping in x2apic mode" ('x2apic' can be different on old CPUs, but should still work)

如果没有，可以允许不安全中断(unsafe interrupts)
``` bash 
echo "options vfio_iommu_type1 allow_unsafe_interrupts=1" > /etc/modprobe.d/iommu_unsafe_interrupts.conf
```

5. 查看和确认设备地址
查看iommu_groups

![](https://minio.kevin2li.top/image-bed/blog/20230528165617.png)

查看设备名称

![](https://minio.kevin2li.top/image-bed/blog/20230528165742.png)


6. 向虚拟机中添加PCI设备

编辑`/etc/pve/qemu-server/{vmid}.conf`(vmid替换为目标虚拟机编号，如101)  

在文件最后添加下面内容：

``` bash 
# 添加一个pci设备
hostpci0: 01:00.0

# 添加多个pci设备
hostpci0: 01:00.0;01:00.1
```

保存后，在网页上勾选`PCI-Express`

![](https://minio.kevin2li.top/image-bed/blog/20230528170631.png)

==未成功==

- USB直通  

参考：https://pve.proxmox.com/wiki/USB_physical_port_mapping
