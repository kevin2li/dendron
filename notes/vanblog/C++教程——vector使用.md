# Cheat sheet
>参考：https://hackingcpp.com/cpp/std/vector.html

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/9b40ca380c70d7fa131b1235def7128c.image.png)

<!-- more -->

# 初始化

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/8f9aa6ee6784786498bb6838de3b82e2.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/61b1669a7bc2b67d85d520c9339f5a76.image.png)

# 属性查询
## 获取长度、容量、为空
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/71e91bdefe7b826032155be1235093d3.image.png)

# 访问元素(查)
## 根据下标

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/eaec31c8e7db4a20e2077ca511262915.image.png)

## 首尾元素

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/3b4e16ad7709beeaaf011df9482547f3.image.png)


# 添加元素(增)
## 尾部追加

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/90544569feec3baeb2688cb213fb972b.image.png)

## 中间插入

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/61adc15573ed3ca9ce430d5803cdaa2c.image.png)

## 指针范围插入

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1e6e0b5db20e6a7abe4a899870f3a4b5.image.png)

## 插入构造类型元素

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a8063a3569448601353daabb5de3f04b.image.png)

# 删除元素(删)
## 删除尾部

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/3961a0097290e938389dbc3b3c8f886c.image.png)

## 清空

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5f7defe00a06fa489c8167464427fc24.image.png)

## 指针(范围)删除

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a414c6f9c83c3bb7dcbb7872da742c9e.image.png)

# 修改元素(改)
## assign

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d15cc9b245ed94ffee5595e7db0968f1.image.png)

# 遍历元素
## 方式1：基于range（推荐）

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b8b370ef3ee5ccf7e755228f9e24d7c7.image.png)

## 方式2：基于iterators
1. 正向遍历
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/986063e5225b76f85a1ebf7ad8ec1cf6.image.png)

2. 反向遍历
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/9a67c4c6ef04e57c8de69c1853405fd6.image.png)

## 方式3：基于indices

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b9d20ef2ab75520d8b3b147690cf0fc6.image.png)

# 高级
## 容量增长策略

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4de700a2a9bf0971b92ae01e75a55d24.image.png)