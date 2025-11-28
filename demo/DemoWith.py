"""
with 关键字, 上下文管理器
简化资源管理, 确保代码执行前和执行后, 可靠的执行特定的操作(比如打开文件释放资源, 获取锁释放锁)
"""
from contextlib import contextmanager

# 使用with管理文件资源
with open("temp.txt", "r", encoding="UTF-8") as file:
    read = file.read()
    print(read)
# 文件在with后自动释放, 无论是否异常

# with 工作原理, __enter__() 和 __exit__()
# __enter__(): 程序执行到with, 调用上下文管理器对象的 __enter__(), 并将方法返回值赋值给 as 后的变量
# 执行with的代码块
# __exit__(): with代码块执行完毕或发生异常中断, 调用上下文管理器的 __exit_(), 这个方法负责释放资源, 还可以处理异常

"""
# with expression [as variable]:
#     with-block
# 实际上大致相当于：
mgr = expression # 获取上下文管理器对象
exit_function = type(mgr).__exit__ # 获取 __exit__ 方法
value = type(mgr).__enter__(mgr)   # 调用 __enter__ 方法
exc = True
try:
    try:
        # 如果有 as variable，则 variable = value
        # 执行 with-block
    except:
        # 如果发生异常
        exc = False
        if not exit_function(mgr, *sys.exc_info()): # 调用 __exit__ 并传递异常信息
            raise # 如果 __exit__ 返回 False，则重新抛出异常
finally:
    if exc: # 如果没有发生异常或者 __exit__ 处理了异常
        exit_function(mgr, None, None, None) # 正常调用 __exit__
"""
print("------------------------")

"""
自定义上下文管理器
1.定义类实现 __enter__() 和 __exit__()
2.使用 contextlib.contextmanager 装饰器, 利用生成器函数
"""


class MyContextManger:
    def __init__(self, name):
        self.name = name
        print(f"初始化管理器: {self.name}")

    def __enter__(self):
        print(f"进入上下文: {self.name}")
        # 返回需要使用的对象, 赋值给with as的变量名
        return self

    """
    exc_type: 异常类型 (如果没有异常则为 None)
    exc_val: 异常实例 (如果没有异常则为 None)
    exc_tb: 异常回溯 (如果没有异常则为 None)
    返回值: 如果返回 True，则忽略异常；否则，异常会继续传播。
    """

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"退出上下文: {self.name}")
        if exc_type is not None:
            print(f"上下文中异常: {exc_type.__name__}: {exc_val}")
            return False
        return None  # 这里通常返回None, 表示不处理任何异常, 让异常传播


# 使用自定义上下文管理器
with MyContextManger("My管理器测试") as cm:
    print(f"with代码块执行: {cm.name}")


print("------------------------")


# 利用生成器函数实现
@contextmanager
def my_context(name):
    # try 之前, 对应 __init__()
    print(f"初始化管理器: {name}")
    # 假定访问文件
    t_file = "假定open()"
    try:
        # yield之前, 对应__enter__()
        print(f"进入上下文管理器: {name}")
        yield t_file
        # yield 之后的代码（在 try 块内）对应 __exit__ 的正常退出部分
        print(f"正常退出上下文")
    except Exception as e:
        # except代码块, 对应
        print(f"上下文中异常: {type(e).__name__}: {e}")
        # 通常情况下, 上下文中的异常需要重新抛出
        raise
    finally:
        # finally 块中的代码总是会执行，对应 __exit__ 的清理工作
        # 对应 __exit__()
        print(f"finally清理资源: {name}")


# 使用自定义生成器
with my_context("My生成器测试") as cm:
    print(f"with代码块执行: {cm}")
    raise RuntimeError("强制异常")
