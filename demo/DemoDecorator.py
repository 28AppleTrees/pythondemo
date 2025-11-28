import functools
import math

"""
装饰器
    核心概念: 函数func作为参数, 并返回可调用的函数对象
    注意: 通常情况functools要在所有装饰器使用
定义语法:
    def my_decorator(source_func):  # 装饰器函数
        def inner_func(*args, **kwargs):  # 装饰器内部包装函数, 参数非必须, 但通常内部包装函数可以接收任意参数
            print("inner_func-start")
            source_func(*args, **kwargs)  # 执行原函数
            print("inner_func-end")
        return inner_func  # 返回内部包装函数, 注意返回函数对象不能有`()`
应用语法:
    在需要被装饰的方法上, 使用`@my_decorator`
使用语法:
    正常调用原方法 source_func() 即可
"""

"""基础装饰器"""


# 定义一个装饰器, 返回的内部包装函数为inner_func(), 参数func为被装饰的函数
def my_decorator(func):
    # 内部包装函数, 参数非必须, 但通常内部包装函数可以接收任意参数, 使用 *args, **kwargs
    def inner_func(*args, **kwargs):
        print("内部包装函数执行-start")
        # 执行原函数, 传递全部参数, source_result接收原函数执行结果
        source_result = func(*args, **kwargs)
        print("内部包装函数执行-end")
        return source_result

    return inner_func  # 返回可调用的内部包装函数, 注意返回函数对象不能有`()`


# 使用`@`应用装饰器, 定义另一个普通函数normal_func(), 装饰normal_func()
@my_decorator
def normal_func():
    print("普通函数执行...")
    return


# 调用被装饰的普通函数normal_func(), 具体执行逻辑为装饰器内 inner_func()
normal_func()
print("--------------------")

"""使用functools装饰器"""


# 定义装饰器2
def my_decorator2(func):
    @functools.wraps(func)  # functools.wraps装饰器, 保留原函数的元信息(__name__等)
    def inner_func(*args, **kwargs):
        print("内部包装函数执行-start")
        source_result = func(*args, **kwargs)
        print("内部包装函数执行-end")
        return source_result  # 返回原函数执行结果

    return inner_func  # 返回内部包装函数


@my_decorator2
def normal_func2(arg):
    print(f"普通函数2执行...参数: {arg}")
    return "普通函数2"


normal_func2("参数2")
print(f"未使用functools.wraps: {normal_func.__name__}")  # 输出: inner_func, 原函数信息丢失, 变为
print(f"使用functools.wraps: {normal_func2.__name__}")  # 输出: normal_func2, 原函数信息保留
print("--------------------")

"""
使用带参数装饰器
装饰器如果需要携带参数, @decorator(参数)
python规定了`@`后只能是无参装饰器 或 有参装饰器, 而有参装饰器不允许func和其他参数混用, 必须要再包一层用于接收装饰器的参数
"""


# 定义带参数装饰器
def my_decorator3_factory(arg):
    print(f"装饰器工厂接收到参数: {arg}")

    def my_decorator3(func):  # 真实的装饰器
        print(f"真实装饰器执行: {func.__name__}")

        @functools.wraps(func)
        def inner_func(*args, **kwargs):
            print("内部包装函数执行-start")
            source_result = func(*args, **kwargs)
            print("内部包装函数执行-end")

        return inner_func  # 返回内部包装函数

    return my_decorator3  # 返回真实的装饰器


@my_decorator3_factory("工厂参数")
def normal_func3(arg):
    print(f"普通函数3执行...参数: {arg}")
    return "普通函数3"


normal_func3("参数3")
print("--------------------")

"""
常用内置装饰器
"""

"""
@property: 将一个类的方法转换为一个只读属性, 调用这个属性时, 其实执行了方法
@属性.setter: 必须配合@property, 可以自定义修改属性值的函数
@属性.deleter: 显式控制属性删除行为, 少见, 常见场景: 资源清理 状态重置

注意: 在使用@属性.setter, 赋值和获取必须使用下划线 `_属性` 进行操作底层属性, 否则会递归setter
"""


class Circle:

    def __init__(self, radius):
        self.radius = radius  # 初始化, self.radius会调用 setter
        # self._radius = radius  # 初始化, self._radius不会调用 setter

    # 将area()转换为一个属性area
    @property
    def area(self):
        """计算圆的面积"""
        return math.pi * self._radius ** 2

    """
    具体原理:
    @property 装饰器会将其下方的 radius 函数包装成一个 property 对象。这个对象本身定义了如何“获取”值（通过 fget 参数关联到原来的 radius 函数）。
    @radius.setter 装饰器则会找到前面已经创建的那个 property 对象（通过 radius 这个名字），然后将下面这个同名的 radius 函数作为“设置”值的方法（通过 fset 参数关联到这个 property 对象中）。
    最终, Circle 类的命名空间中只有一个名为 radius 的对象，但它是一个特殊的 property 实例, 该实例自动调用获取和赋值函数
    """

    # 这里定义重名的方法, python解释器会在执行时, 判断时获取还是赋值, 执行不同的逻辑
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        print(f"setter赋值: {value}")
        self._radius = value  # 必须使用下划线 `_属性` 赋值底层属性, 否则会递归调用setter


circle1 = Circle(2)
print(f"@property, 圆的面积: {circle1.area}")
# circle1.area = 10  # @property默认只读, 在未定义setter时, 无法赋值给area

circle1.radius = 3
print(f"@property, 圆的面积: {circle1.area}")
print("--------------------")

"""
@staticmethod: 将一个方法标记为静态方法, 可以直接通过类名调用
注意: 静态方法不接收默认的第一个参数(如self或cls)
"""


class MyUtil:

    @staticmethod
    def add(x, y):
        """一个加法函数示例"""
        return x + y


print(f"@staticmethod, 工具类加法: {MyUtil.add(1, 2)}")
print("--------------------")

"""
@classmethod: 将一个方法标记为类方法, 类方法接收一个指向 类本身 的隐含参数(通常命名为cls), 而不是实例对象self
常用于创建工厂方法替代构造方法, 访问或修改类属性
"""


class MyClass:
    class_param = "类属性"

    def __init__(self, arg):
        self.arg = arg
        super().__init__()

    @classmethod
    def get_class_param(cls):
        return cls.class_param

    @classmethod
    def build_by_str1(cls, str1):
        return MyClass(str1)  # 工厂方法, 返回类实例

# 通过静态方法也可以访问类属性, 类方法访问的优点是, 被继承时, cls指向的是子类class
print(f"@classmethod, 访问类属性: {MyClass.get_class_param()}")
print(f"@classmethod, 工厂方法构建实例: {MyClass.build_by_str1("自定义str1").arg}")
print("--------------------")



"""
@functools.lru_cache(): 缓存, 相同的入参返回相同的结果, 在缓存后, 不会执行方法体, 直接返回缓存结果
"""


@functools.lru_cache()
def cache(arg):
    print(f"执行缓存方法, 入参:{arg}")
    return "缓存结果"


print(cache(1))
print(cache(1))  # 本次调用不会输出方法体内的输出, 直接获取缓存结果

print(f"cache方法当前缓存数据: {cache.cache_info()}")  # CacheInfo(hits=1, misses=1, maxsize=128, currsize=1)
