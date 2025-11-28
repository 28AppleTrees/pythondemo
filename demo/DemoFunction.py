"""
函数
格式:
# 函数名(形参)
def function_name(param):
    # 函数体
    print("函数体")
    # 返回值, 可选, 无返回值默认返回 None
    return "返回值"
"""
import itertools
from functools import reduce


def simple_demo(num1, num2):
    return num1 + num2


# 默认参数
# 注意, 默认参数必须放在非默认参数后
def default_param(str1, str2="default"):
    print(f"str1: {str1}, str2: {str2}")


default_param("1")  # str1: 1, str2: default
default_param("1", "2")  # str1: 1, str2: 2
print("--------------------------------------")


# 不定长参数
# *: 表示任意数量参数, 存入元组; **: 表示任意数量参数, 存入字典
# 注意, 形参定义*必须在**之前
def any_param(*args, **dict_args):
    print(f"元组参数: {args};; 字典参数: {dict_args}")


# 不定长参数函数调用
any_param(0, "a", [], k1="v1", k2="v2")
any_param(1, 2, 3)  # 只传元组
any_param(k3="v3", k4="v4")  # 只传字典
# 解包传参
num_list = [1, 2, 3]
dict1 = {"k5": "v5"}
# 错误写法, 不使用*和**解包时, 会将num_list整体作为第一个参数, dict1整体作为第二个参数
any_param(num_list, dict1)  # 元组参数: ([1, 2, 3], {'k5': 'v5'}); 字典参数: {}
# 正确写法, * 和 ** 用于解包
any_param(*num_list, **dict1)
print("--------------------------------------")


# 列表, 字典, 不定长参数组合
def any_param2(fix_list, fix_dict, *args, **dict_args):
    print(f"固定列表: {fix_list}")
    print(f"固定字典: {fix_dict}")
    print(f"可变列表: {args}")
    print(f"可变字典: {dict_args}")


any_param2([1, 2, 3], {"fixK": "fixV"}, "a", "b", "c", dict_key="dict_value")
print("--------------------------------------")

"""
lambda匿名函数
语法: lambda arguments: expression
注意:
    只能有一个表达式
    表达式的结果为函数的返回值
"""
# 定义lambda函数
lambda_sum = lambda x1, x2: x1 + x2
print(f"lambda求和: {lambda_sum(1, 0.1)}")

"""
常用函数
"""
num_list = [1, 2, 3, 4, 5]
str_list = ["a", "bb", "ccc", None, ""]
# map(func, iterable), 将可迭代对象的所有元素调用func, 返回<class 'map'>, 是迭代器
demo_map = map(lambda x: str(x + 1), num_list)
print(f"map(): {list(demo_map)}")

# filter(func, iterable), 将可迭代对象调用func, 返回<class 'filter'>, 是迭代器
demo_filter = filter(lambda x: x % 2 == 0, num_list)
print(f"filter(): {list(demo_filter)}")

demo_filter2 = filter(None, str_list)  # func=None, 等于过滤掉 False等价物
print(f"filter2(): {list(demo_filter2)}")

# reduce(func, iterable[, init]), func必须接收2个参数, 将参数可迭代对象每次按照func运算, 运算后的结果再次与下一个元素运算
demo_reduce = reduce(lambda x, y: x + y, num_list)  # 列表内元素+运算
print(f"reduce(): {demo_reduce}")
# reduce()如果指定了init初始值, 则作为运算的初始值
demo_reduce2 = reduce(lambda x, y: x + y, num_list, 10)
print(f"reduce2(init): {demo_reduce2}")

# sorted(iterable, *, key, reverse=False), 将可迭代对象通过key函数排序, 返回一个新列表
# * 为特殊函数定义语法, 表示*后的参数传值时必须指定key, 不能按照顺序传值
demo_sorted = sorted(num_list, reverse=True)
print(f"sorted(): {demo_sorted}")
demo_sorted2 = sorted(filter(None, str_list), key=len, reverse=True)  # 按照长度倒序, 列表含None, 会报错
print(f"sorted2(): {demo_sorted2}")
# python三元运算: <value_true> if <condition> else <value_false>
# 先判断x is not None, True则执行表达式len(x), False则执行表达式-1
demo_sorted3 = sorted(str_list, key=lambda x: len(x) if x is not None else -1, reverse=True)
print(f"sorted3(): {demo_sorted3}")

# itertools模块
str_list = ["abcde"]
print(list(itertools.chain(*str_list)))


