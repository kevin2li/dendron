---
id: x3vly0r66r1l0wfts7rbdmh
title: vscode插件开发教程
desc: ''
updated: 1686894830059
created: 1686357655503
---


## 简介
xx

参考：
1. [快速上手](https://code.visualstudio.com/api/get-started/your-first-extension)
1. [VS Code API](https://code.visualstudio.com/api/references/vscode-api#api-namespaces-and-classes)
2. [Contribution Points](https://code.visualstudio.com/api/references/contribution-points)
3. [Activation Events](https://code.visualstudio.com/api/references/activation-events)


## 方法
### 流程
1. 在`packages.json`中声明命令
``` json 
"contributes": {
  "commands": [
    {
      "command": "helloworld.helloWorld",
      "title": "Hello World"
    }
  ]
},
```

2. 在`extension.ts`中注册命令和订阅命令

``` ts 
let disposable = vscode.commands.registerCommand('helloworld.helloWorld', () => {
  // The code you place here will be executed every time your command is executed

  // Display a message box to the user
  vscode.window.showInformationMessage('Hello World!');
});

context.subscriptions.push(disposable);
```


### 常用代码

- 获取当前选择文本
``` ts
function getSelectedText(): string | undefined {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    return undefined;
  }
  const selection = editor.selection;
  if (selection.isEmpty) {
    return undefined;
  }
  const document = editor.document;
  return document.getText(selection);
}

```

- 替换指定范围文本

``` ts
const range = new vscode.Range(
  lineNumber,
  index1,
  lineNumber,
  column + index2 + 2
);
editor.edit((editBuilder) => {
  editBuilder.replace(range, newText);
}); 
```

- 获取当前行号和列号

``` ts
const document = editor.document;
const lineNumber = editor.selection.active.line; // 获取当前行号
const position = editor.selection.active;
const column = position.character;  //获取当前列号
const lineText = document.lineAt(lineNumber).text; // 获取当前行的文本 
```

### 打包

``` json 
  "scripts": {
    "compile": "node ./esbuild.js",
    "package": "NODE_ENV=production node ./esbuild.js",
    "watch": "node ./esbuild.js --watch",
    "lint": "eslint src --ext ts",
    "vscode:prepublish": "npm run esbuild-base -- --minify",
    "esbuild-base": "esbuild ./src/extension.ts --bundle --outfile=out/main.js --external:vscode --format=cjs --platform=node",
    "vsce-package": "pnpm vsce package --no-dependencies",
    "vsce-publish": "pnpm vsce publish --no-dependencies"
  },
```

``` bash 
npm install -g vsce
```

### 查看已安装插件运行日志

1. 控制台日志  

`Ctrl+Shift+P`: `Developer: Toggle Developer Tools`

![](https://minio.kevin2li.top/image-bed/blog/20230616135132.png)


2. 文件日志

`Ctrl+Shift+P`: `Developer: Open Extension Logs Folder`


## 参考