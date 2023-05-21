# 方法
## 选项1：访问不存在的键会报错
- 写法1：
```python
class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


my_dict = {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}

new_dict = AttributeDict(my_dict)

print(new_dict.website)  # 👉️ bobbyhadz.com
print(new_dict.topic)  # 👉️ Python

new_dict.author = 'Borislav Hadzhiev'

# 👇️ {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python', 'author': 'Borislav Hadzhiev'}
print(new_dict)

del new_dict.author

# 👇️ {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}
print(new_dict)

```

<!-- more -->

- 写法2：
```python
class AttributeDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self


my_dict = {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}

new_dict = AttributeDict(my_dict)


print(new_dict.website)  # 👉️ bobbyhadz.com
print(new_dict.topic)  # 👉️ Python

# ✅ add a key to the dictionary
new_dict.author = 'Borislav Hadzhiev'

# 👇️ {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python', 'author': 'Borislav Hadzhiev'}
print(new_dict)

# ✅ delete a key from the dictionary
del new_dict.author

# 👇️ {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}
print(new_dict)

```

## 选项2：访问不存在的键返回None
```python
class AttributeDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


my_dict = {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}

new_dict = AttributeDict(my_dict)

print(new_dict.example)  # 👉️ None

print(new_dict.website)  # 👉️ bobbyhadz.com
print(new_dict.topic)  # 👉️ Python
```

## 选项3: 支持嵌套字典
```python
class Struct:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__dict__[key] = Struct(**value)
            else:
                self.__dict__[key] = value


my_dict = {
    'name': {
        'first': 'bobby',
        'last': 'hadz',
    },
    'website': 'bobbyhadz.com'
}

obj = Struct(**my_dict)

print(obj.name.first)  # 👉️ bobby
print(obj.name.last)  # 👉️ hadz
print(obj.website)  # 👉️ bobbyhadz.com

```

# 参考
1. https://bobbyhadz.com/blog/python-use-dot-to-access-dictionary