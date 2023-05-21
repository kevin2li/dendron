# 简介
Pandas是一个Python库，用于数据操作和数据分析。它提供了一种名为DataFrame的数据结构，该结构类似于电子表格或SQL表。Pandas还提供了许多用于数据操作和分析的函数和方法，例如：

- 读取和写入各种文件格式的数据
- 数据清洗和预处理
- 数据转换和重塑
- 数据聚合和分组
- 时间序列分析
- 绘图
- ...

**学习资源**：  
- 用户手册：https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide  
- API参考：https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api

<!-- more -->

# 教程

## DataFrame基本操作
### 创建
```python
df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/58334d019017c02de2fd935e5207590e.image.png)

### 查看数据
- `df.head()`：查看顶部5行(默认)
- `df.tail()`：查看底部5行(默认)
- `df.index`: 查看索引

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5b85efacbb6502cea99c8e2aac19d490.image.png)

- `df.columns`: 查看包含的列

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/f7920cad8cf0330e0fcbc8e4195bb746.image.png)

- `df.shape`: 查看形状

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e8680b05d5a4f184c4634b0e2c061333.image.png)

- `df.dtypes`: 查看每列的数据类型

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/48c966ba040eeb95a4854161cbce3174.image.png)

- `df.describe()`: 查看每列数据的统计特征(均值、标准差、最小值、最大值、分位点等)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d935ca94c77236f8659340ee822147d1.image.png)


### 合并
- `pd.concat`
```python
out_df = pd.concat([df1, df2])
```

### 筛选
### 筛选指定行

```python
# 根据index查
df.loc[0]
df.loc[[0,2]]

# 根据编号查
df.iloc[1]

```
### 筛选指定列

```python
# 筛选一列
df['a']

# 筛选多列
df[['a', 'c']]
```

### 筛选指定行指定列
```python
df.loc[0:2,['A', 'C']]

df.loc[df['a'] > 10, ['a’, 'c']]
```

### 条件筛选
- `[]`筛选
```python
df[df['Length']>7]                      # 基本
df[(df['Length']>7) & (df['Width']<8)]  # 与
df[(df['Length']>7) | (df['Width']<8)]  # 或
df[~(df['E']=='train')]                 # 非
df[df['Name'].str.startswith("abc")]    # 字符串
df[df['E'].isin(['train', 'test'])]     # 列表
```
- `df.query`
```python
df.query('Length > 7')
df.query('Length > 7 and Width < 8')
df.query('Name.str.startswith("abc")', engine="python")
```

:::info{title="多个条件组合"}

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/fe59b99c5155c3ed941625f334502b86.image.png)

:::

### 修改
- `df.assign()`
- `df.apply()`

## 排序
- `df.sort_values()`

## 分组
- `df.group_by()`

## 统计相关
- `df.sum()`
- `df.min()`
- `df.max()`
- `df.mean()`
- `df.median()`
- `df.std()`
- `df.var()`
- `df.count()`: 统计每列(行)的非NA值数量

## 缺失值处理
- `df.dropna()`
- `df.fillna(value)`

## 去重
- `df.drop_duplicates()`

## 画图
- `df.plot.hist()`
- `df.plot.scatter(x='w', y='h')`

# 参考
[1] [Pandas_Cheat_Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
