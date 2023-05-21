# 简介
环境变量存储操作系统和其他程序使用的数据。 例如， `WINDIR` 环境变量包含 Windows 安装目录的位置。 程序可以查询此变量的值，以确定 Windows 操作系统文件所在的位置。

PowerShell 可以访问和管理任何受支持的操作系统平台中的环境变量。 借助 PowerShell 环境提供程序，可以在当前控制台中获取、添加、更改、清除和删除环境变量。

<!-- more -->

# 方法
涉及到三个参数：
- `env_name`: 环境变量名称
- `env_value`: 环境变量的值，始终存储为字符串，不能为空
- `env_scope`: 环境变量的范围  

在 Windows 上，可以在三个范围内定义环境变量：

- 计算机 (或系统) 范围：`Machine`
- 用户范围: `User`
- 进程范围: 包含当前进程或 PowerShell 会话中可用的环境变量。 此变量列表继承自父进程，是从计算机和用户范围内的变量构造的


:::warning{title="注意：`System.Environment`方法才能永久更改环境变量"}
在 PowerShell 中更改环境变量时，更改仅影响当前会话。 此行为类似于 Windows Command Shell 中命令的行为 `Set` 和基于 UNIX 的环境中的 `Setenv` 命令的行为。 若要更改`Machine` 或 `User` 作用域中的值，必须使用 `System.Environment` 类的方法。  
若要对计算机范围(`Machine`)的变量进行更改，还必须具有管理员权限。
:::

## 设置和修改环境变量
语法：
```powershell
[Environment]::SetEnvironmentVariable(env_name, env_value, env_scope)
```

示例：
```powershell
# 设置JAVA_HOME环境变量
[Environment]::SetEnvironmentVariable('JAVA_HOME', 'C:\Program Files\Java\jdk-11.0.13' , 'Machine')

# 设置PATH环境变量
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\Program Files\Go\bin\", "Machine")
```

## 查询环境变量
语法：
```powershell
# 方法一：
$Env:<env_name>

# 方法二：
[Environment]::GetEnvironmentVariable(env_name, env_scope)
```

## 删除环境变量
语法：
```powershell
[Environment]::SetEnvironmentVariable(env_name, '', env_scope)
```
示例：
```powershell
[Environment]::SetEnvironmentVariable('Foo', '', 'Machine')
```

# 参考
1. [使用 PowerShell 永久修改环境变量](https://zhuanlan.zhihu.com/p/424377493)  
2. [ about_Environment_Variables](https://learn.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2)