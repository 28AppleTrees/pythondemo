from collections.abc import Iterable, Iterator

"""
迭代器和生成器
迭代器:
    是一个对象, 用于逐个访问 列表 集合 字典等 容器中的元素
    迭代器必须实现两个方法:
        __iter__(): 返回当前对象的迭代器
        __next__():返回迭代器中下一个元素, 如无更多元素, 抛出异常 StopIteration
    注意: iter() 每次调用返回的都是新的迭代器对象
    注意: iter()对象 通常只能访问一次, 但可自定义迭代器特殊逻辑可重复访问
生成器:
    一种特殊的迭代器,
    是一个`函数`, 关键字 yield 替换 return, 调用包含 yield 的函数时, 不会像普通函数那样执行并返回值, 而是返回一个生成器对象
    注意: 惰性计算, 生成器只有在需要时才计算下一个值, 节省内存
"""


class Countdown:
    """
    自定义迭代器类, 注意区分可迭代对象
    标准可迭代器对象只需要实现__iter__(), 并在方法返回新的迭代器实例
    """

    # 倒计时迭代器, 从start开始
    def __init__(self, start):
        self.current = start

    # 返回迭代器对象本身
    def __iter__(self):
        return self

    def __next__(self):
        # 倒计时结束, 抛出迭代结束异常
        if self.current < 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1  # 返回递减前的值


countdown = Countdown(5)
for i in countdown:
    print(i)
print("---二次遍历---")
for i in countdown:  # 不会有任何输出, 因为迭代器已经被消耗
    print(i)

# --- 示例 1: list 是可迭代对象，但不是迭代器 ---
my_list = [1, 2, 3]
print(isinstance(my_list, Iterable))  # True - list 是可迭代的
print(isinstance(my_list, Iterator))  # False - list 本身不是迭代器

list_iterator = iter(my_list)  # 通过 iter() 获取迭代器
print(isinstance(list_iterator, Iterable))  # True - 迭代器也是可迭代的
print(isinstance(list_iterator, Iterator))  # True - list_iterator 是迭代器

# --- 示例 2: 生成器是迭代器 ---
gen = (x for x in range(3))
print(isinstance(gen, Iterable))  # True - 生成器是可迭代的
print(isinstance(gen, Iterator))  # True - 生成器是迭代器


# --- 示例 3: 自定义可迭代对象 ---
class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        # 返回一个全新的迭代器实例
        return MyRangeIterator(self.start, self.stop)


class MyRangeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self  # 迭代器的 __iter__ 返回自身

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            val = self.current
            self.current += 1
            return val


my_range = MyRange(1, 3)
print(isinstance(my_range, Iterable))  # True - MyRange 是可迭代的
print(isinstance(my_range, Iterator))  # False - MyRange 本身不是迭代器

my_range_iterator = iter(my_range)  # 获取迭代器
print(isinstance(my_range_iterator, Iterable))  # True - 迭代器是可迭代的
print(isinstance(my_range_iterator, Iterator))  # True - 这是迭代器


# --- 关系总结 ---
# 1. 每个迭代器 (Iterator) 都是可迭代对象 (Iterable)
#    (因为 Iterator 是 Iterable 的子类型)
# 2. 并非每个可迭代对象 (Iterable) 都是迭代器 (Iterator)
#    (例如 list, str, dict 等)


def demo_generator():
    """
    自定义生成器
        生成器自动处理生成器的状态, 遇到yield
    """
    print("生成器start")
    yield 1  # 每次yield时函数暂停执行, 返回yield后的元素
    print("生成器after 1")
    yield 2
    print("生成器after 2")
    yield 3
    print("生成器end")


generator = demo_generator()
print("生成器第一次获取: ", end="")
print(next(generator))
print("生成器第二次获取: ", end="")
print(next(generator))
print("生成器第三次获取: ", end="")
print(next(generator))
print("生成器第四次获取: ", end="")
print(next(generator))  # 输出"生成器end", 然后 StopIteration 异常
