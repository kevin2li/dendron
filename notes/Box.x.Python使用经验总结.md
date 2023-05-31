---
id: k9i42xs3cwf1y2j6imt4b10
title: Python使用经验总结
desc: ''
updated: 1685512695260
created: 1685512413863
---

## 自定义包导入路径设置
假设项目根目录下有个`src`目录，当导入`scr.some_pkg`失败时，可以将根目录加入到`site-packages`的环境变量中。
``` bash 
# 在项目根目录下执行(tqdm是环境下确认安装过的包名，也可以换成其他)
echo $PWD >>  $(pip show tqdm|awk -F: '/Location/ {print $2}')"/my.pth"
```