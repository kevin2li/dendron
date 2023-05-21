# 简介
拼音输入法应该是年轻人用的最多的输入法了，使用简单方便，依托各大输入法强大的词库联想功能，大大提高了打字效率。但是为了追求极致的打字速度，很多人还会纠结使用9键还是26键快，各执一词谁也说服不了谁。但其实大家用的拼音输入法基本都是全拼输入法，在不借助联想功能的情况下需要完整敲击拼音的每个字母才能录入文字，事实上还有另一种拼音输入法以减少击键次数来达到提升打字速度的目的，也是我们今天的主角——双拼输入法。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b178bdd410413eb88664238e11750a15.image.png)


双拼输入法是使用两个字母对汉字进行编码的方案，第一个字母表示声母，第二字母表示韵母，也就是说任何一个汉字使用两次敲击就可以打出，相比全拼在按键次数上有明显优势，并且上手难度也比五笔输入法小得多，熟悉全拼的人可以很快入门。

双拼输入法也有很多种编码方案，如小鹤双拼、自然码双拼等，大家可根据喜好自行选择一种即可。本人使用的是小鹤双拼，其键位图如上图所示。

小鹤双拼官网：https://www.flypy.com/  


<!-- more -->
# 安装
windows系统也内置了双拼方案，但是没有小鹤双拼，下面介绍如何在windows中使用小鹤双拼。

1. 新建一个`小鹤双拼.reg`的注册表文件，内容如下：
```bash
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS]
"Enable Double Pinyin"=dword:00000001
"DoublePinyinScheme"=dword:0000000a
"Expand Double Pinyin"=dword:00000000
"UserDefinedDoublePinyinScheme0"="小鹤双拼*2*^*iuvdjhcwfg xmlnpbksqszxkrltvyovt"
```
2. 双击运行上面的`小鹤双拼.reg` (以管理员权限运行)

# 启用
可以在“设置”中查看和启用

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a25ec28b7b656eb562fe46ef58bf4abf.image.png)