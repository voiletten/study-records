'''
# 全局缓存字典（所有被装饰函数共用同一个cache）
cache = {}

def cache_func(func):
    def wrapper(*args):
        # 判断参数元组是否存在缓存
        if args in cache:
            return cache[args]
        # 不存在则执行原函数
        res = func(*args)
        # 存入缓存
        cache[args] = res
        return res
    return wrapper

# 装饰等价于 big_calc = cache_func(big_calc)
@cache_func
def big_calc(a,b):
    print("复杂计算中...")
    return a**b

@cache_func
def add(a,b):
    return a + b

print(big_calc(3,2))
print(cache)
print(add(3,2))
print(cache)
'''


# 类装饰器实现缓存管理
class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self._cache = {}

    def __call__(self, *args):
        if args in self._cache:
            return self._cache[args]
        res = self.func(*args)
        self._cache[args] = res 
        return res
    
    def clear(self):
        self._cache.clear()
        print("缓存已清空")
    
    #新增获取缓存的方法
    def get_cache(self):
        return self._cache

@CacheDecorator
def big_calc(a,b):
    print("复杂计算中...")
    return a**b

@CacheDecorator
def add(a,b):
    return a + b

print(big_calc(3,2))
print(big_calc.get_cache())
print(add(3,2))
print(add.get_cache())
big_calc.clear()
print(big_calc.get_cache())
print(add.get_cache())
# print(big_calc._cache)

