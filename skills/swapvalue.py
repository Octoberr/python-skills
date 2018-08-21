"""
Python骚操作
create by swm
20180821
"""

# 查找列表中频率最高的值
def getthefrequentelement():
    a = [1, 2, 2, 3, 5, 7, 1, 1, 1]
    # print(max(set(a), key=a.count))
    from collections import Counter
    cnt = Counter(a)
    print(cnt.most_common())
    return

def sorteddict():
    d = {'apple': 10, 'orange': 20, 'banana': 5, 'tomatto': 1}
    # print(d.items())
    print(sorted(d.items(), key=lambda x: x[1]))
    return

def setstrlist():
    from collections import OrderedDict
    items = ["foo", "bar", "bar", "foo"]
    print(list(OrderedDict.fromkeys(items).keys()))
    return


if __name__ == '__main__':
    # getthefrequentelement()
    # sorteddict()
    setstrlist()