import os,sys
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# print(BASE_DIR)

# def decorator(func):  # 创建一个装饰器函数，接受的参数arg参数就是func函数名
#     def inner(*args, **kwargs):
#         print("执行函数之前")
#         ret = func(*args, **kwargs)
#         print("执行函数之后")
#         return ret
#     return inner
# @decorator  # 如果要让某个函数使用装饰器，只需要在这个函数上面加上@+装饰器名
# def func(arg):
#     print(arg)
# func("Hello World!")

def parameter(a, b):
    print(a, b)
    def decorator(func):
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return decorator
@parameter(1, 2)
def func(a, b):
    return a + b
print(func(10, 20))