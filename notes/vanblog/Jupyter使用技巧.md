# 简介
本文主要介绍Visual Studio Code中的Jupyter插件的使用技巧。

# 常用技巧
1. 多行输出显示
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

2. pandas显示行数设置
```python
# 显示全部行
pd.set_option('display.max_rows', None) # 也可以指定具体行数
```

<!-- more -->
