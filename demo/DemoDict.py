"""
字典, 存储键值对
字典通过`{}`表示, 每个键值对通过`:`表示对应关系, 多个键值对通过`,`分隔
键值对的key必须为可哈希的且唯一, 元组可作为字典key(元组内无可变元素)
自定义类无__eq__()或__hash__()时, 默认基于对象id进行哈希, 可以作为key
"""
dict_empty = {}  # 空的字典
dict1 = {"key1": "v1", 2: "v2"}
print("输出字典", dict1)
# 访问字典值
print("访问字典", dict1[2])  # 注意, 如果直接访问一个不存在的key, 会报错 Traceback (most recent call last): KeyError:

# 添加字典, 赋值一个不存在的key
dict1[(1, 2)] = "v3"
print("添加字典:", dict1)

# 修改字典, 赋值一个已存在的key
dict1["key1"] = "vEdit"
print("修改字典:", dict1)

# 删除字典键值对, 如果key不存在, 报错KeyError
del dict1[(1, 2)]
print("删除字典:", dict1)

# 清空字典, 删除整个字典
dict1.clear()
print("清空字典:", dict1)
del dict1  # 删除后无法操作, 注释

"""
常用方法
"""
dict2 = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 字典长度len()
print("字典长度len():", len(dict2))

# keys(), values(), items 返回值为视图对象, 可以通过list转换后使用
print("dict.keys():", dict2.keys())  # 输出 dict_keys(['k1', 'k2', 'k3'])
print("dict.keys()->list:", list(dict2.keys()))  # 输出 ['k1', 'k2', 'k3']
print("dict.values():", dict2.values())
print("dict.items():", dict2.items())


# 循环
# dict.items(), 可以获取key和value
for k, v in dict2.items():
    print(k, ":", v)

# iter() 或直接 for k in dict, 只能获取key
# for k in iter(dict2):
#     print(k)

# 安全获取get(), key存在, 返回value; key不存在时返回默认值, 不会异常
print("安全获取get()1:", dict2.get("k1", "默认值"))
print("安全获取get()2:", dict2.get("k4", "默认值"))

# 安全删除pop(), key存在, 删除并返回value; key不存在时返回默认值, 不会异常
print("安全删除pop()1:", dict2.pop("k1", "默认值"))
print("安全删除pop()2:", dict2.pop("k1", "默认值"))

# 函数更新update(), key存在更新; key不存在, 新增键值对
# update() 参数可以是元组(只能是2个元素)和字典, 表示将所有数据更新到字典
dict2.update({"k2": "v2Edit"})
print("函数更新update()1:", dict2)
dict2.update([("kXx", "vXx")])
print("函数更新update()2:", dict2)

# 函数新增setdefault(), key不存在, 新增键值对; key存在, 返回value
print("函数新增setdefault()1:", dict2.setdefault("k2", "默认值"))
print("函数新增setdefault()2:", dict2.setdefault("kXxx", "默认值"))
print(dict2)
