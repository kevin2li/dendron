# 简介
asdf 是一个跨平台的版本管理器，可以用来管理多种编程语言的版本，包括 Node.js、Python、Ruby、Elixir、Java、Rust、Go、Haskell 等等。它的主要功能是方便地在同一系统上安装、管理和切换不同版本的编程语言和相关工具。

以下是一些 asdf 的主要特点和用法：

- 管理多种编程语言：asdf 支持管理多种编程语言的版本，而不是只支持单一语言。这对于需要使用多种语言的开发人员来说非常方便。
- 管理多个版本：asdf 可以在同一系统上安装和管理多个版本的每种编程语言。你可以随时切换不同版本，以满足不同项目的需求。
- 简单易用：asdf 的安装和使用非常简单，只需要在终端运行几个命令即可开始使用。
- 自定义插件：asdf 支持自定义插件，这意味着你可以轻松地添加或删除特定语言或工具的插件。这样你可以将它用作一个通用的工具，以管理不同语言的版本和相关工具。

文档：https://asdf-vm.com/guide/getting-started.html

<!-- more -->

# 使用



以下是安装和使用 asdf 的基本步骤：

1. 安装 asdf：在终端中运行以下命令来安装 asdf：

```
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.1
echo -e '\n. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo -e '\n. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc
source ~/.bashrc
```

2. 安装插件：在终端中运行以下命令来安装特定语言或工具的插件。例如，要安装 Node.js 插件，请运行以下命令：

```
asdf plugin-add nodejs
```

3. 安装特定版本：在终端中运行以下命令来安装特定版本的语言或工具。例如，要安装 Node.js 的 14.16.0 版本，请运行以下命令：

```
asdf install nodejs 14.16.0
```

4. 设置全局版本：在终端中运行以下命令来设置全局语言或工具的版本。例如，要设置全局 Node.js 版本为 14.16.0，请运行以下命令：

```
asdf global nodejs 14.16.0
```

5. 切换版本：在终端中运行以下命令来切换特定项目使用的语言或工具版本。例如，要切换当前项目使用的 Node.js 版本，请运行以下命令：

```
asdf local nodejs 14.16.0
```

总之，asdf 是一个非常有用的跨平台版本管理器，可以帮助开发人员方便地管理多个语言和工具