---
id: tfpfzdee1pmqy56r46xvo1x
title: Anki使用教程
desc: ''
updated: 1686399512530
created: 1686121375245
---

## 简介
Anki是一款流行的开源记忆卡片软件，它可以帮助用户有效地学习和记忆各种知识。Anki最初是为学习日语而开发的，但现在已经成为学习各种学科和主题的工具。

Anki的基本原理是使用记忆卡片来帮助用户记忆信息。用户可以创建自己的卡片，将问题放在一面卡片上，答案放在另一面。当用户学习时，Anki会根据用户的回答情况，调整卡片出现的频率和顺序，以帮助用户更有效地记忆信息。

Anki还提供了一些高级功能，如支持图像、音频和视频等多媒体内容，以及支持插件和第三方工具的集成。用户可以在Anki官方网站上下载各种预制卡片模板，或者自己创建自定义模板。

Anki目前可用于Windows、MacOS、Linux、iOS和Android等多个平台。它是一款非常实用的工具，适用于各种学习场景，比如学习语言、医学、编程、历史、地理等各个领域。

官网：https://apps.ankiweb.net/  
AnkiWeb: https://ankiweb.net/about  

常用插件
- AnkiConnect: https://ankiweb.net/shared/info/2055492159  
- Image Occlusion Enhanced： https://ankiweb.net/shared/info/1374772155
- Markdown and KaTeX Support：https://ankiweb.net/shared/info/1087328706
- custom sync server redirector： https://ankiweb.net/shared/info/358444159
- Cloze (Hide All)：https://ankiweb.net/shared/info/1709973686

## 方法
### 卡片制作

- 选择题

- 填空题

可以借助vscode快速插入填空插槽，打开`keybindings.json`(Preferences: Open Keyboard Shortcuts File)，在里面添加下面内容：
``` json
{
    "key": "ctrl+shift+1",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
        "snippet": "{{c1::${TM_SELECTED_TEXT}}}"
    }
} 
```
这样当选中关键文本后，按快捷键`Ctrl+Shift+1`就可以将选中的文字转换为anki可以识别的填空插槽。


### subtitle2

### subtitle3

## 参考