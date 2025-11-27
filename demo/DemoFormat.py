"""
format关键字符:
`^`:居中
`<`:左对齐, 右补位
`>`:右对齐, 左补位
`:`:后指定单个且只能单个字符, 表示补位时占位符, 未指定时默认为空格
`{}`:需要用到{}括起来时, 可以使用两侧{{}}
"""
# format格式化
print("format格式化: {}|{}".format("a", "b"))
# format格式化:kv
print("format k-v参数: {key1}|{key2}".format(key1="value1", key2="value2"))

# format格式化:字典
dict_demo = {"key1": "value1", "key2": "value2"}
print("format 字典参数: {key1}|{key2}".format(**dict_demo))

# format格式化:列表
# 注意, 出现异常时, 将无法输出, 未捕获异常时程序暂停执行
list_demo = ["data1", "data2", "data3"]
try:
    print("format 列表参数: {0[0]}|{0[2]}".format(list_demo))  # 0[0], 列表作为参数时, 前缀`0`必须有
except IndexError as e:
    print("format 列表参数异常!!!")


# format格式化:对象
class ClassDemo(object):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


class_demo = ClassDemo("classV1", "classV2")
print("format 对象参数: {0.value1}|{0.value2}".format(class_demo))
print("format 对象参数: {obj.value1}|{obj.value2}".format(obj=class_demo))
# f-string
print(f"format 对象参数: {class_demo.value1}|{class_demo.value2}")

# format数值格式化, 默认 四舍六入五成双
print("保留0位,2位,3位小数格式化: {:.0f}|{:.2f}|{:.3f}".format(1.5, 0.525, 0.12345))
print("带符号数值格式化: {:+f}|{:-f}".format(0.12545, -0.12345))

# format数值补位
print("format数值左侧补零: {:0>3}".format(9))  # 009
print("format数值右侧补零: {:0<3}".format(9))  # 900
print("format数值左侧补任意字符: {:n>3}".format(9))  # nn9

print("format数值`,`格式: {:,}".format(1000000))  # 1,000,000

# format数值百分比, {:.n} n表示转为百分数后的小数位, 不足时补零
print("format数值百分比1: {:%}".format(1))  # 100.000000%
print("format数值百分比2: {:.0%}".format(0.2))  # 20%
print("format数值百分比3: {:.3%}".format(0.2))  # 20.000%
