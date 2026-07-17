class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0  # 实例属性永久保存计数

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数 {self.func.__name__} 已调用 {self.count} 次")
        return self.func(*args, **kwargs)

    # 拓展自定义方法：外部可主动查看次数
    def get_count(self):
        return self.count

@CallCounter
def hello():
    print("Hello World")

hello()
hello()
hello()
# 外部调用装饰器实例的方法
print("总调用次数：", hello.get_count())