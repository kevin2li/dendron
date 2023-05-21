# 简介
Windows 终端是一个新式主机应用程序，它面向你喜爱的命令行 shell，如命令提示符、PowerShell 和 bash（通过适用于 Linux 的 Windows 子系统 (WSL)）。 它的主要功能包括多个选项卡、窗格、Unicode 和 UTF-8 字符支持、GPU 加速文本呈现引擎，你还可用它来创建你自己的主题并自定义文本、颜色、背景和快捷方式。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2af769a2d6358c5d0ca7c172e4f07410.image.png)

文档：https://learn.microsoft.com/zh-cn/windows/terminal/  
GitHub: https://github.com/microsoft/terminal

<!-- more -->

# 使用

1. 设置选项卡标题，禁止自动更改选项卡标题

> 问题背景： 可以在这里设置选项卡打开时的标题，但是马上又会被自动替换为其他名称，如`~`。我不想被替换，怎么办？

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/04e37a44f20f02362debdc60697d8800.image.png)

点击左下角`Open JSON file`，将会打开一个名为`settings.json `的配置文件，找到目标机器的配置位置，然后加入下面这行：
```bash
"suppressApplicationTitle": true,
```

如图：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e3889ac84158666650162a6884cfce94.image.png)