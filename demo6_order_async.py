import asyncio
import time

# async def compute(name, x):              # ← 注意多了 async
#     await asyncio.sleep(1)         # ← 注意用 await 和 asyncio.sleep
#     print(f"{name} 的结果是 {x*2}")
async def fetch(name, delay):              # ← 注意多了 async
    await asyncio.sleep(delay)         # ← 注意用 await 和 asyncio.sleep
    return (f"{name} 完成")


async def main():
    start = time.time()
    # gather 并发执行多个任务
    result = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 3),
    )
    end = time.time()
    print(f"耗时：{end - start} 秒")  # ← 注意用 end - start
    print(result)

asyncio.run(main())  # ← 总开关，启动
