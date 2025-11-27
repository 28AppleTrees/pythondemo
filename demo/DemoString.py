str_1 = "0123456789"
# 字符串可以 双引号 单引号 包含, 否则就需要使用\转义
str_2 = "123'abc'456"
# 字符串可以多行, 通过 `'''` 或 `"""`
str_3 = '''多行文本
多行文本'''

# print输出多个内容, 默认通过 空格` ` 分割
print("str_1:", str_1)
print("str_2:", str_2)
print("str_3:", str_3)
# 字符串切割[start:end:step], start包含, end不包含, step表示步长
print("[0:1]:", str_1[0:1])

# 输出索引1: 之后所有
print("[1:]:", str_1[1:])

# python内字符串, 两种索引, 左到右0开始, 右到左-1开始
print("[0:-1]:", str_1[0:-1])

# 输出1-9的字符串, 并且步长为2(即每隔一个字符输出): 13579
print("[1:10:2]:", str_1[1:10:2])

# 字符串通过 `+` 可以拼接
print("A" + "B" + "C")

# 字符串通过 `*` 重复
print(("A" + "B" + "C") * 2)

# 输出多个字符串时, sep指定分隔符, 默认是空格
print("str1", "str2", sep="|")

# in / not in 字符串包含判断
print("`a`在`abc`中:", "a" in "abc")
print("`ac`在`abc`中:", "ac" in "abc")
print("`ac`不在`abc`中:", "ac" not in "abc\n")

# r/R 原始字符串, 转义字符 特殊字符也依据文本输出, 在字符串引号前添加r/R
print("原字符串:", "a\tb\nc")
print("r/R原始字符串:", r"a\tb\nc")

# f-string只能左侧补位:{value:fill align width} align取值:`<`=左对齐右侧补; `>`=右对齐左侧补; `^`=居中
print("f-string左侧补零:", f"{9:03}")
print("f-string左侧补任意:", f"{9:n>3}")  # nn9
print("f-string居中补任意:", f"{9:n^5}")  # nn9nn
