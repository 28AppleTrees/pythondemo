"""
集合, 无序 唯一
使用`{}`创建集合, 元素用`,`分隔
"""
# 创建空集合, 必须用set(), `{}`为空字典
set_empty = set()

set1 = {"a", "b", "c", "a"}
print("无序唯一:", set1)

set2 = set("cde")  # 创建了集合 {'c', 'd', 'e'}
print("set1:", set1)
print("set2:", set2)
# set1存在set2不存在
print("set1 - set2:", set1 - set2)
# set1和set2所有元素
print("set1 | set2:", set1 | set2)
# 交集
print("set1 & set2:", set1 & set2)
# 差集, 不同时存在两个的元素
print("set1 ^ set2:", set1 ^ set2)
# 计算并直接赋值, -= |= &= ^=
set1 -= set2
print("set1 -= set2", set1)

# 添加元素, 只支持单个元素
set1.add((1, 2))  # 添加了单个元素(1, 2)
print("添加元素add():", set1)
# 添加多个元素, 可以是元组, 列表, 字典(字典仅添加key)
set1.update((1, 2, 3))  # 添加了多个元素:1,2,3
print("添加元素update()1:", set1)
set1.update({"k1": "v1"})  # 添加了字典的key:k1
print("添加元素update()2:", set1)
set1.update({"k2": "v2"}.items())  # 添加了键值对元组:('k2', 'v2')
print("添加元素update()3:", set1)

# 移除元素remove(), 不存在时会异常 KeyError: '不存在的值'
set1.remove((1, 2))
print("移除元素remove():", set1)
# 移除元素discard(), 不存在时不会异常
set1.discard("不存在的值")
print("移除元素discard():", set1)


