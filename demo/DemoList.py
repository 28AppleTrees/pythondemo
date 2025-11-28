import operator
import copy

"""
列表
"""
# 使用`[]`括起来, `,`分割, 可以有不同类型
list_t = [1, 'a', []]

# 截取, 索引[start:end), 左开右闭, 索引也可以从尾部'-1'开始
list1 = [1, 2, 3, 4, 5]
print("原始列表:", list1)
print("列表截取[1:3]:", list1[1:3])
print("列表截取[1:]:", list1[1:])  # 从指定索引开始截取到末尾

# 添加
list1.append(6)
print("列表添加:", list1)

# 删除, 通过索引
del list1[5]
print("列表删除:", list1)

# 更新, 通过索引
list1[0] = 'a'
print("列表更新:", list1)
list1[0] = 1

"""
列表比较
"""
# 列表比较需要引入 operator 模块的 eq 方法
print("列表比较:", operator.eq(list1, list_t))

"""
常用
"""
# 长度len()
print("列表长度len():", len(list1))

# 组合`+`
print("列表组合`+`:", list1 + list1)

# 重复`*n`
print("列表重复`*n`:", list1 * 3)

# 元素是否存在列表in
print("元素是否存在列表`in`:", 1 in list1)

# 循环迭代遍历
print("列表循环:", end="")  # print(end=)表示该输出结束后追加的内容, 未指定时默认为`\n`
for e in list1:
    print(e, end=" ")
print()

# 最大值max(), 最小值min()
# 除少数例外(int和float), 列表内不同类型不能直接比较, 报错TypeError
# Number类型按照大小比较
list2 = [1, 2, 3]
print("列表最大值:", max(list2))
print("列表最小值:", min(list2))
# String类型按照unicode顺序, unicode中大写字母在小写前, 所以'Abc'更小
list2 = ['abc', 'bcd', 'Abc', '啊']
print("列表最大值:", max(list2))
print("列表最小值:", min(list2))
# 自定义比较
print("列表自定义比较最小长度:", min(list2, key=len))
# 自定义提取比较
list2 = [
    {"key": 10},
    {"key": 30},
    {"key": 20}
]
# key=lambda t: t['key'] 表示 指定key比较, 比较值的来源是 t(定义每个元素, 这里是dict), t['key'](获取每个元素对应key的值)
print("列表自定义提取比较最大值:", max(list2, key=lambda t: t['key']))  # 输出{'key': 30}, 因为对应dict的值30最大
list2 = [
    ("user1", "男", 10),
    ("user2", "女", 20),
    ("user3", "武装直升机", 30)
]
# key=lambda t: t['key'] 表示 指定key比较, 比较值的来源是 t(定义每个元素, 这里是tuple), t[2](获取每个元素对应索引2的值)
print("列表自定义提取比较最大值:", max(list2, key=lambda t: t[2]))  # 输出("user3", "武装直升机", 30), 因为对应元组索引[2]的30最大

# 尾部添加append()
list1.append("append")
print("列表尾部添加append:", list1)

# 元素次数统计count()
print("列表元素次数统计:", list1.count(1))

# 元素定位index(), 该值匹配的第一个索引
print("列表元素定位:", list1.index(2))

# 插入元素insert(index, obj), 在指定索引插入元素, 其他元素顺位后移, 可使用负数索引
list1.insert(0, 'a')
print("列表插入元素:", list1)

# 移除元素pop(index), 未填索引时默认-1, 即最后一个元素, 返回值为移除元素
pop = list1.pop()
print("列表移除元素:{}, 结果:{}".format(pop, list1))

# 移除元素remove(obj), 移除首个匹配元素, 无返回值
# 移除元素在列表不存在时, 会报错, 推荐使用try catch ValueError, 因为remove() 和 if in 都会进行遍历, 直接try remove()只遍历一次
list1.remove("a")
print("列表移除元素remove():", list1)

# 移除元素列表推导, 使用元组进行移除判断, 效率更高, 且不会报错
"""
格式:[<expression> for <item> in <iterable> if <condition>]
[ ... ]
    表示我们正在创建一个新的列表。
x（<expression>）:
    这是最终放入新列表的元素表达式, 保留原始元素 x, 可以转为其他obj
for x in my_list（<item> in <iterable>）:
    循环，遍历 my_list 中的每一个元素, 在每次循环中，把当前元素赋值给变量 x
if x not in to_remove（<condition>）:
    过滤条件, x not in to_remove 为 True 时，才会执行前面的 <expression>（也就是 x），并把 x 加入到新列表中。
"""
to_remove = ("1", "a")  # 定义要移除的多个元素为元组
list1 = [x for x in list1 if x not in to_remove]  # 输出[1, 2, 3, 4, 5], 因为"1"和1不是一个类型
print("列表移除元素推导:", list1)

# 列表排序sort(key, reverse), 修改原列表, key:指定一个函数, 该函数会作用于列表内所有元素, 返回值作为排序依据; reverse:指定是否倒序
list1.sort(key=None, reverse=False)
print("列表排序:", list1)
list_sort = [
    {"key": 10},
    {"key": 30},
    {"key": 20}
]
list_sort.sort(key=lambda d: d['key'], reverse=False)
print("列表排序:", list_sort)
list_sort = [
    ("user1", "男", 10),
    ("user2", "女", 20),
    ("user3", "武装直升机", 30)
]
list_sort.sort(key=lambda user: user[2], reverse=True)  # list2内是元组, 这个sort()表示取每个元组内索引2的值排序
print("列表排序:", list_sort)

# 清空列表
list1.clear()
print("列表清空:", list1)

# 复制列表copy()和deepcopy()
list_copy1 = ["a", "b", ["c"]]
list_copy2 = list_copy1.copy()
list_copy3 = copy.deepcopy(list_copy1)
list_copy1[2][0] = "cc"  # 此时已经复制, 修改索引2的元素列表
"""
浅拷贝只会复制顶层元素, 对于非引用对象复制值, 引用对象则复制索引
需要注意的是 元组 为不可变元素, 即使浅拷贝也会创建新的元组, 不影响新列表
"""
print("列表copy:", list_copy2)
print("列表deepcopy:", list_copy3)

# 列表嵌套
list3 = [1, 2, [1, 2, 3]]
print("列表嵌套:", list3[2][2])  # 输出3

