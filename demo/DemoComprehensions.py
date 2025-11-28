"""
推导式:
列表推导式 (List) 最常用
字典推导式 (Dict)
集合推导式 (Set)
生成器表达式 (Generator Expression)
"""

"""
列表推导式
语法结构: [expression for item in iterable if condition]
    expression: 对 item(每个元素对象) 执行的操作或变换，结果将作为新列表的一个元素
    item: 来自迭代器迭代的每个元素
    iterable: 任何可迭代的对象
    condition(可选): 过滤条件, 满足条件的 item 才会被处理并收集到新列表
"""
# 列表推导式: 基础用法
# 获取偶数的平方
# 传统循环方式
res1 = []
for e in range(10):
    if e % 2 == 0:
        res1.append(e**2)
# 推导式
res2 = [e**2 for e in range(10) if e % 2 == 0]
print(f"基础用法res1: {res1}")
print(f"基础用法res2: {res2}")
print("------------------------------------")

# 列表推导式: 嵌套循环
# 生成两个列表所有笛卡尔积
res1 = []
list1 = ["a", "b"]
list2 = [1, 2]
for letter in list1:
    for num in list2:
        res1.append((letter, num))

# 推导式
res2 = [(letter, num) for letter in list1 for num in list2]
print(f"嵌套循环: {res1}")
print(f"嵌套循环: {res2}")
print("------------------------------------")

# 列表推导式: 表达式变换
# 转大写, 并统计长度
word_list = ["hello", "world"]
word_info = [(word.upper(), len(word)) for word in word_list]
print(f"表达式变换: {word_info}")
print("------------------------------------")

"""
字典推导式
语法结构: {key_expression: value_expression for item in iterable if condition}
    key_expression: 生成键的表达式
    value_expression: 生成值的表达式
    item: 同列表推导式, 来自迭代器迭代的每个元素
    iterable: 同列表推导式, 任何可迭代的对象
    condition: 同列表推导式
"""
# 字典推导式: 基础用法
# 从键值对创建字典
pairs = [("name", "张三"), ("age", 10), ("sex", "男")]
# 传统循环方式
res3 = {}
# 这里直接迭代了列表的元组对象, 使用的是多重赋值的一种方式, 序列解包
# 序列解包时, 会将可以迭代的元组对象, 按顺序赋值给左侧的 k, v
for k, v in pairs:
    res3[k] = v
print(f"基础用法: {res3}")
# 推导式
res4 = {k: v for k, v in pairs}
print(f"基础用法: {res3}")

# 交换键和值
dict1 = {"k1": "v1", "k2": "v2"}
dict2 = {v: k for k, v in dict1.items()}  # 注意这里使用.items()获取key和value, 字典默认的iter()无法获取值
print(f"基础用法: {dict2}")

# 使用zip()合并两个列表
# zip(iter_obj1, iter_obj2, ...)接收任意个可迭代对象, 依次取对应索引位置的元素生成一系列元组
# zip()基于最短序列生成, 其他可迭代对象超出的元素不会处理
# zip()返回值为迭代器, 需要通过list(zip())转为列表查看, 或者直接使用迭代器
list1 = ["x", "y", "z"]
list2 = [1, 2, 3, 4]
for e in zip(list1, list2):  # ('x', 1),('y', 2),('z', 3),
    print(e, end=", ")
res5 = {k: v for k, v in zip(list1, list2)}  # {'x': 1, 'y': 2, 'z': 3}
print(f"\nzip(): {res5}")
print("------------------------------------")

"""
集合推导式
语法结构: {expression for item in iterable if condition}
    与列表推导式用法相同, 需要注意集合的无序性和唯一性, 且使用`{}`, 列表使用`[]`
"""
list3 = ["a", "b", "c", "a"]
# 通过集合推导式转大写并去重
res6 = {e.upper() for e in list3}  # {'A', 'B', 'C'}
print(f"集合推导式: {res6}")
print("------------------------------------")

"""
生成器表达式
语法结构: (expression for item in iterable if condition)
    注意 使用`()`, 在函数内调用省略括号
    注意 生成器返回值为一个generator(生成器对象), 其他推导式直接返回生成的列表,集合或字典
    注意 生成器惰性求值, 只有在使用时才计算下一个值, 节省内存, 用于处理大量数据或无限序列
    注意 生成器只能取值一次就会耗尽, 无法再次使用
"""
# 创建一个平方列表
# 列表推导式
# 直接创建了<class 'list'>实例, 包含所有元素
list4 = [e**2 for e in range(10)]
print(f"列表推导式创建, type: {type(list4)}; list4: {list4}")
# 生成器表达式
# 创建了<class 'list'>实例, 只是一个轻量的生成器对象, list4: <generator object <genexpr> at 0x000001D6A5818E10>
list5 = (e**2 for e in range(10))
print(f"生成器表达式创建, type: {type(list5)}; list4: {list5}")
# 首次使用生成器
print("首次使用生成器: ", end="")
for t in list5:
    print(t, end=", ")
# 再次使用生成器, 无法获取到元素
print("\n再次使用生成器: ", end="")
for t in list5:
    print(t, end=", ")
print("------------------------------------")

"""
生成器使用方式
注意:
    生成器被使用或消费后, 无法再次获取其中元素
    len()函数无法用于生成器, 因为生成器是惰性的
    sum(iterable), max(iterable), min(iterable), all(iterable): (消费整个生成器)
    any(iterable): any()找到首个True的元素就短路返回了, 消费部分生成器
    sorted(iterable): 对元素进行排序(消费整个生成器)
    list(iterable), tuple(iterable), set(iterable), dict(iterable): 强制生成所有元素(消费整个生成器)
"""
long_range = range(1000_0000)  # 一个很大的范围
# 生成器表达式, 只创建一个轻量级的生成器对象, 不占用内存
long_generator = (e for e in long_range)
# 逐个获取值
print("生成器逐个获取值:")
print(next(long_generator))  # 0
print(next(long_generator))  # 1
print(next(long_generator))  # 2














