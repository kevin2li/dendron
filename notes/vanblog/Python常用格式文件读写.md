# 常用格式读写
## json
- 读
```python
def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)
```
- 写
```python
def save_json(obj, path):
    with open(path, 'w') as f:
        json.dump(obj, f)
```

<!-- more -->

## csv
- 读
```python
# common reader
def read_csv(filename: str):
    with open(filename, "r", newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        for i, row in enumerate(reader):
            print(row)

# dict reader
def read_csv(filename: str):
    with open(filename, "r", newline='') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            print(row)
```

- 写

```python
# common writer
with open("temp.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    row = ["model", "weight", "ckpt_path"]
    writer.writerow(row)
    f.flush()

# dict writer
with open("temp.csv", "w", newline="") as f:
    header = ["model", "weight", "ckpt_path"]
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    item = {
        "model": 'HGT',
        'ckpt_path': 'aaa.ckpt',
    }
    writer.writerow(item)
```
## yaml
- 读

```python
def read_yaml(filename: str):
    with open(filename, "r") as f:
        obj = yaml.safe_load(f)
        return obj
```

- 写
## ini

## jsonl

## pickle

## torch
- 读
```python
# 普通读取
torch.load('tensors.pt')

# 指定映射设备
torch.load('tensors.pt', map_location=torch.device('cpu'))
```

- 写
```python
x = torch.tensor([0, 1, 2, 3, 4])
torch.save(x, 'tensor.pt')
```
## dgl
- 读
```python
# 单张图
graph_path = "fsl_graph.dgl"
(g, ), _ = dgl.load_graphs(graph_path)

# 多张图
graph_path = "fsl_graph.dgl"
subgs, labels = dgl.load_graphs(graphs_path)
```

- 写
```python
# 存单张图
dgl.save_graphs("graph.dgl", g)

# 存多张图
dgl.save_graphs("graph.dgl", [g1,g2,g3], {"label": [0,1,2]})
```

# 格式转换
## csv转jsonl
```python
import csv
import jsonlines
from tqdm import tqdm

def count_lines(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count

def count_lines(filename):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    with open(filename, 'r') as f:
        bug_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None))
        return sum(buf.count("\n") for buf in buf_gen)

def csv_to_jsonl(csv_path: str, jsonl_path: str, row_type: str = 'dict'):
    """converts a CSV file to jsonlines format
    Args:
        csv_path (str): the path to the CSV file
        jsonl_path (str): the path to the output jsonlines file
        row_type (str, optional): row type of the output jsonlines file. Defaults to 'dict'.
    """
    total = count_lines(csv_path)
    with open(csv_path, "r", newline='') as f, jsonlines.open(jsonl_path, mode='w') as writer:
        reader = csv.DictReader(f)
        if row_type == 'dict':
            for i, row in tqdm(enumerate(reader), total=total):
                writer.write(row)
        elif row_type == 'list':
            for i, row in tqdm(enumerate(reader), total=total):
                writer.write(list(row.values()))
        else:
            raise ValueError("unsupported row type: %s, `dict` or `list` are expected!" % row_type)
```
