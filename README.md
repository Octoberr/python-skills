# python-skills
Some interesting and useful python skills.

### 交换变量值
```python
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)
```

### 将列表中所有的元素组合成字符串
```python
a = ["python", "is", "awesome"]
print(" ".join(a))
```

###查找列表中频率最高的值
```python
a = [1, 2, 2, 3, 5, 7, 1, 1, 1]
print(max(set(a), key=a.count))
"""
Use Counter from collections
"""
from collections import Counter
cnt = Counter(a)
print(cnt.most_common(3))
# 3 代表取前3个
```

### 检查两个字符串是不是由相同字母不同顺序组成
```python
from collections import Counter
str1 = "sadassa"
str2 = "sadasas"
resbool = Counter(str1) == Counter(str2)
print(resbool)
```

### 反转字符串或反转列表
```python
a = "sadsadkslad"
a = [1, 2, 3, 4, 8]
print(a[::-1])
print(reversed(a))
```

### 转置二维数组
```python
#transpose 2d array [[a, b], [c, d], [e, f]] -> [[a, c, e], [b, d, f]]
original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transpose = zip(*original)
print(list(transpose))
```

### 通过键排序字典元素
```python
d = {'apple':10, 'orange': 20, 'banana': 5, 'tomatto': 1}
print(sorted(d.items(), key=lambda x: x[1]))

from operator import itemgetter
print(sorted(d.items(), key=itemgetter(1)))

print(sorted(d, key=d.get))
```

###For Else
```python
a = [1, 23, 34, 5, 4]
for el in a:
    if el == 0:
        break
else:
    print('did not break the loop.')
```

###转换列表为逗号分割格式
```python
items = ['foo', 'bar', 'xyz']
print(','.join(items))
numbers = [2, 3, 5, 10]
print(','.join(map(str, numbers)))
```
### 合并字典
```python
d1 = {'a':1}
d2 = {'b':2}
d1.update(d2)
```
###列表中最大值和最小值的索引
```python
lst = [40, 10, 20 ,30]
def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)
def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)
```

### 移除列表中重复的元素
```python
items = [1, 2, 2, 2, 3]
newitem = list(set(items))

from collections import OrderedDict
items = ["foo", "bar", "bar", "foo"]
print(list(OrderedDict.fromkeys(items).keys()))
```

