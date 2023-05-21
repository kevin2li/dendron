# 简介

参考：[SQL教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1177760294764384/1179610846971200)
<!-- more -->

# 基本语法
# 数据查询
### 基本查询
```sql
SELECT * FROM <表名>
```

### 条件查询
```sql
SELECT * FROM <表名> WHERE <条件表达式>
```

### 投影查询
```sql
SELECT 列1, 列2, 列3 FROM <表名> WHERE <条件表达式>
```
### 排序
```sql
SELECT id, name, gender, score FROM students ORDER BY score;
```
### 分页查询
把结果集分页，每页3条记录。要获取第1页的记录
```sql
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 0;
```

### 聚合查询
```sql
SELECT COUNT(*) num FROM students;
SELECT AVG(score) average FROM students WHERE gender = 'M';
```

### 分组查询
```sql
SELECT class_id, COUNT(*) num FROM students GROUP BY class_id;
```

### 多表查询
```sql
SELECT
    students.id sid,
    students.name,
    students.gender,
    students.score,
    classes.id cid,
    classes.name cname
FROM students, classes;
```

### 连接查询
```sql
SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
FROM students s
INNER JOIN classes c
ON s.class_id = c.id;
```

## 数据增加

## 数据修改

## 数据删除
