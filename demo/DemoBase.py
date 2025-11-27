"""
基础控制
"""
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
a = 1
if a == 1:
    print("a == 1")
elif a == 2:
    print("a == 2")
else:
    print("a不等于1或2")

"""
条件控制 match case
注意: 3.10版本后可以使用
"""
# 基础匹配
match a:
    case 1:
        print("match case 1")
    case 2:
        print("match case 2")
    case _:
        print("_默认匹配")

