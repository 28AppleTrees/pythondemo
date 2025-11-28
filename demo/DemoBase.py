"""
条件控制 if elif else
"""
# if可以直接判断对象,值为True, 数值类型时0为False
if "1":
    print("直接判断String1=True")
if "0":
    print("直接判断String0=True")

if 1:
    print("直接判断Number1=True")

if 0:
    pass
else:
    print("直接判断Number0=False")

# if判断分支控制
num = 1
if num == 1:
    print("num == 1")
elif num == 2:
    print("num == 2")
else:
    print("num不等于1和2")

"""
条件控制 match case
python中case语句没有穿透的概念, 不需要每个分支后break
注意: 3.10版本后可以使用
"""
num = 1
# 基础匹配 case _ 表示通配符
match num:
    case 1:
        print(f"{num} match case 1")
    case 2:
        print(f"{num} match case 2")
    case _:
        print(f"{num} match case 通配符")

# 使用if
match num:
    case n if n < 0:
        print(f"{num} < 0")
    case n if n % 2 == 0:
        print(f"{num}是偶数")
    case n if n % 2 != 0:
        print(f"{num}是奇数")


# 匹配序列(序列模式), 列表/元组, 注意序列模式中 ()和[]等价
# 定义一个match方法
def match_list(point):
    match point:
        case []:
            print("匹配空列表")
        case (0, 0):  # 匹配元组(0, 0)
            print("匹配原点坐标(0, 0)")
        case (x, y):  # 匹配任意2个元素的序列, 元组和列表都可以
            print(f"匹配二维坐标({x}, {y})")
        case (x, y, z):  # 匹配任意3个元素的序列, 元组和列表都可以
            print(f"匹配三维坐标({x}, {y}, {z})")
        case [*items]:  # 明确匹配任意长度列表
            print(f"匹配列表: {items}")
        case (first, *items):
            print(f"匹配元组至少含一个元素: first={first}, items={items}")
        case items:  # 捕获模式(会在上方条件不满足时捕获所有情况), 将所有元组捕获到items变量
            print(f"其他所有情况: {items}")


print("------------match匹配序列------------")
match_list((0, 0))
match_list([])
match_list([1])
match_list([1, 2])
match_list((0, 1))
match_list({"k": "v"})
print("------------match匹配序列------------")


# 匹配字典(映射模式), 映射模式中{}会匹配所有字典, 需要放到后面的分支
# 定义一个match方法
def match_dict(d):
    match d:
        case {"k1": "v1"}:  # 匹配键值对{k1:v1}
            print(f"匹配键值对k1:v1的字典: {d}")
        case {"code": 200, "data": data}:  # 匹配键值对"code":200, 且含data键, 并把键"data"对应的值赋给data变量
            print(f"匹配到键值对code:200的字典, data: {data}")
        case {}:  # 注意, {}表示任意字典, 宽泛的匹配应该放在更后面的分支
            print("匹配到任意字典")
        case _:
            print(f"匹配到其他数据: {d}")


print("------------match匹配字典------------")
match_dict({})
match_dict({"k1": "v1"})
match_dict({"code": 200, "data": ["id1", "id2"]})
match_dict("code")
print("------------match匹配字典------------")

print("------------match OR匹配------------")
# 匹配`|`OR匹配, 匹配多个 值或模式
param = [0, 1]
match param:
    case 1 | 0 | -1 | "":  # 匹配定值
        print(f"1或0或-1: {param}")
    case (0, _):
        print(f"匹配首元素0, 第二元素任意: {param}")
    case (x, y):  # 不能2长度和3长度写在同一个OR, 需要拆开写
        print(f"匹配长度2序列: {param}")
    case _:
        print(f"其他所有情况:, {param}")
print("------------match OR匹配------------")


class Point:
    def __init__(self, sx, sy):
        self.x = sx
        self.y = sy


class Circle:

    def __init__(self, center, radius):
        self.center = center  # 这里假设center是Point实例
        self.radius = radius


# 匹配对象
def match_obj(obj):
    match obj:
        case Point(x=0, y=0):  # 匹配Point实例, 且x=0,y=0
            print("匹配到中心Point实例(0, 0)")
        case Point(x=sx, y=sy):  # 匹配任意(x, y)Point实例
            print(f"匹配到Point实例({sx}, {sy})")
        case Point():  # 匹配任意Point实例
            print(f"匹配到任意Point实例(null, null)")

        case Circle(center=Point(x=0, y=0), radius=r):
            print(f"匹配到Circle实例1, Point=(0, 0), radius={r}")
        case Circle(center=Point(x=cx, y=cy), radius=r):
            print(f"匹配到Circle实例2, Point=({cx}, {cy}), radius={r}")
        case Circle(center=center, radius=r):
            print(f"匹配到Circle实例3, Point=({center}), radius={r}")
        case Circle():  # 匹配任意Circle实例
            print(f"匹配到任意Circle实例4")
        case _:
            print("匹配到其他情况")


p1 = Point(0, 0)
p2 = Point(0, 1)
match_obj(p1)
match_obj(p2)
match_obj(Circle(p1, 0))
match_obj(Circle(p2, 0))
match_obj(Circle(None, 0))
match_obj(Circle(None, None))


"""
多重赋值示例
`=`左侧赋值的目标是`,`分隔时, python解释器会将`=`右侧作为值序列打包, 同时赋值, 该语句为原子性操作
`=`右侧必须为可迭代对象, 即定义了__iter__() 和 __getitem__() 方法, iter()就可以创建迭代器
`=`左侧未使用`*`时, 左右两侧数量必须一致, 使用`*`表达式后, 优先赋值给固定参数, 多余的值会依据值顺序打包为序列
"""
a = 1
b = 2
# 多重赋值, 不经过临时变量
print(f"多重赋值前:a:{a}, b:{b}")
a, b = b, a
print(f"多重赋值后:a:{a}, b:{b}")
a, b, c = [1, 2, 3]  # 列表多重赋值
print(f"列表多重赋值:a:{a}, b:{b}, c:{c}")
a, b, c = {"k1": "v1", "k2": "v2", "k3": "v3"}  # 字典多重赋值, 只会取字典的key,
print(f"字典多重赋值:a:{a}, b:{b}, c:{c}")
a, b, c = "abc"  # 字符串序列多重赋值
print(f"字符串序列多重赋值:a:{a}, b:{b}, c:{c}")
a, b, c = range(100, 103)  # range()多重赋值
print(f"range()多重赋值:a:{a}, b:{b}, c:{c}")
# 使用`*`表达式后, 多余的值会依据参数定义顺序打包为序列
a, *b, c = range(100, 110)  ## a:100, *b:[101, 102, 103, 104, 105, 106, 107, 108], c:109
print(f"range()多重赋值:a:{a}, *b:{b}, c:{c}")
*a, b, c = "a", 123, ['x', 999], ("tuple1", "tuple2")  # *a:['a', 123], b:['x', 999], c:('tuple1', 'tuple2')
print(f"`*`多重赋值:*a:{a}, b:{b}, c:{c}")


# 多重赋值实现斐波那契数列
print("斐波那契数列n次:", end="")
a, b = 0, 1
for i in range(10):
    print(b, end=",")
    a, b = b, a + b


