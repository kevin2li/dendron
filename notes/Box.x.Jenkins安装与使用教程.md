---
id: b8pngq6l6xv5pvruw62dyas
title: Jenkins安装与使用教程
desc: ''
updated: 1684835026865
created: 1684833826301
---


## 简介
![](https://minio.kevin2li.top/image-bed/blog/20230523173714.png)

Jenkins是一款开源的自动化构建工具，可以帮助开发人员自动化地构建、测试和部署应用程序。Jenkins可以与多种编程语言和技术集成，如Java、Python、JavaScript、Docker等，并提供了丰富的插件和API，可以扩展其功能和定制化需求。Jenkins可以运行在多种操作系统上，如Windows、macOS、Linux等，并提供了Web界面，方便用户进行管理和监控。

Jenkins的主要特点包括：

- **自动化构建**：Jenkins可以自动化地构建应用程序，支持多种构建工具和技术，如Maven、Gradle、Ant、Docker等，并提供了丰富的插件和API，可以扩展其构建功能和定制化需求。

- **持续集成/持续交付（CI/CD）**：Jenkins可以集成CI/CD功能，可以自动化地进行代码检查、构建、测试和部署，提高开发效率和质量。

- **多种集成方式**：Jenkins可以与多种编程语言和技术集成，如Java、Python、JavaScript、Docker等，并提供了丰富的插件和API，可以扩展其功能和定制化需求。

- **多平台支持**：Jenkins可以运行在多种操作系统上，如Windows、macOS、Linux等，可以满足不同平台和环境的需求。

- **可扩展性**：Jenkins提供了丰富的插件和API，可以扩展其功能和定制化需求，满足不同场景的需求。

- **Web界面**：Jenkins提供了Web界面，方便用户进行管理和监控，可以查看构建日志、部署状态、插件信息等。

- **安全和管理**：Jenkins提供了多种安全和管理功能，如用户和权限管理、LDAP集成、安全设置、日志记录等，可以帮助团队更好地管理和保护应用程序和数据的安全。

总之，Jenkins是一款功能强大的自动化构建工具，可以帮助开发人员自动化地构建、测试和部署应用程序，提高开发效率和质量，支持多种集成方式和平台，具有可扩展性和安全性，是现代软件开发中不可或缺的工具之一。

官网: https://www.jenkins.io/  
文档: https://www.jenkins.io/doc/book/  


## 安装
参考: https://www.jenkins.io/doc/book/installing/

### 裸机安装
``` bash 
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```
### docker安装
xx

## 使用

xx
