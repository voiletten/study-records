# 打印函数执行前后日志

# class LogDecorator:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         print(f"=====开始执行函数{self.func.__name__}===========")
#         result = self.func(*args, **kwargs)
#         print(f"=====函数执行结果：result===========")
#         return result

# #使用类作为装饰器

# @LogDecorator
# def add(a, b):
#     return a + b


# @LogDecorator
# def mul(a, b):
#     return a - b


# add(2,3)
# add(5,2)

print("=========================示例2：带参数的类装饰器====================")
class Logger:
    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"[{self.level}]调用函数：{func.__name__}")
            return func(*args, **kwargs)
        return wrapper

# 给装饰器传参
@Logger("DEBUG")
def login(name):
    print(f"登录用户：{name}")

login("张三")