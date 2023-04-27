---
id: y6l8g7qu239x8vs8wkf0as1
title: flask
desc: ''
updated: 1682589614337
created: 1682589602822
---


## 基本示例
```python
from flask import Flask, jsonify
app = Flask(__file__)

@app.route("/hello", methods=['GET'])
def hello():
    return jsonify({"status": "OK", "message": "Hello, world!"})

@app.route("/", methods=['GET'])
def index():
    return jsonify({"status": "OK", "message": "This is index!"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

```
启动：
```bash
flask --app server.py run --host 0.0.0.0 --port 5000 --reload
```

<!-- more -->

## 前端发送数据
```js
// 1. 发送json数据
const data = {
    "a": 1,
    "b": 2,
}
Axios.post('http://127.0.0.1:5000/upload', {
    method: 'post',
    data: data,
})
.then(() => {
    message.success('send successfully.');
})
.catch(() => {
    message.error('send failed.');
});

// 2. 发送formData数据(可用来发送文件)
let formData = new FormData();
formData.append("aaa", "123");
formData.append("bbb", "456");
state.fileList.forEach(file => {
    formData.append('files[]', file.originFileObj as any);
});
Axios.post('/upload', formData, {
    headers: {
        "Content-Type": "multipart/form-data"
        // "Content-Type": "application/x-www-form-urlencoded"
    },
})
.then(() => {
    message.success('upload successfully.');
})
.catch(() => {
    message.error('upload failed.');
});
```
> 如何查看formData数据(直接打印为空)?
```js
// 查看formadata内容
for (var [a, b] of formData.entries()) {
    console.log(a, ":", b);
}   
```

## 后台接收数据
```python
# 路径参数
@app.route('/', methods=['GET', 'POST'])
def index():
    ic(request.args) # 查看所有路径参数
    return jsonify({"result": "ok"})

# 表单类型数据(formData)
@app.route('/', methods=['GET', 'POST'])
def index():
    ic(request.form) # 查看所有表单数据
    default_value = '0'
    data = request.form.get('input_name', default_value)
    return jsonify({"result": "ok"})

# json类型数据
@app.route('/', methods=['GET', 'POST'])
def index():
    json_data = request.get_json(force=True)
    un = json_data['username']
    pw = json_data['password']
    return jsonify({"result": "ok"})

# 文件类型数据
@app.route("/upload/<category>", methods=['POST'])
def upload(category):
    ic(category)
    file = request.files.get('file')
    ic(file)
    save_dir = Path(f"{upload_dir}/{request.remote_addr}/{category}")
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = f"{save_dir}/{file.filename}"
    file.save(save_path)
    return jsonify({"result": "ok"})
```