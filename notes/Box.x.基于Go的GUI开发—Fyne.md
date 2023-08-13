---
id: ivyvhbyjrbmtal14le00dtr
title: 基于Go的GUI开发—Fyne
desc: ''
updated: 1687870745819
created: 1687866726157
---

## 简介

文档：https://developer.fyne.io/started/
github: https://github.com/fyne-io/fyne

![](https://minio.kevin2li.top/image-bed/blog/202306271953114.png)
## 方法

``` bash
go mod init example.com/fyne
go get fyne.io/fyne/v2
go mod tidy
```

``` go
package main

import (
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	a := app.New()
	w := a.NewWindow("Hello")

	hello := widget.NewLabel("Hello Fyne!")
	w.SetContent(container.NewVBox(
		hello,
		widget.NewButton("Hi!", func() {
			hello.SetText("Welcome :)")
		}),
	))

	w.ShowAndRun()
}

```

编译：
``` powershell
# windows(无黑窗口)
go build -ldflags -H=windowsgui .\main.go 

```

### FAQ
1. `build constraints exclude all Go files in...`

![](https://minio.kevin2li.top/image-bed/blog/202306271958690.png)

参考：https://stackoverflow.com/questions/55348458/build-constraints-exclude-all-go-files-in
``` powershell 
$env:CGO_ENABLED=1
go run main
```

## 参考