#异步版
import time
import asyncio

async def task(name):
    # print(f"{name} 开始")
    await asyncio.sleep(1)
    # print(f"{name} 结束")


async def main():
    start = time.time()
    await asyncio.gather(*[task(f"T{i}]") for i in range(10000)])
    print(f"耗时：{time.time() - start} 秒")

asyncio.run(main())


print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

#多线程
import threading
import time

def task(name):
    # print(f"{name} 开始")
    time.sleep(1)
    # print(f"{name} 结束")

start = time.time()
threads = [threading.Thread(target=task, args=(f"T{i}",)) for i in range(10000)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"耗时：{time.time() - start} 秒")