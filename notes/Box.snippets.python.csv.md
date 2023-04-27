---
id: jgyqk2qhmprkb9j6nfa2sf1
title: csv
desc: ''
updated: 1682590149099
created: 1682590108529
---

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