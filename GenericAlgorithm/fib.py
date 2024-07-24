from decimal import Decimal, getcontext

# 设置decimal的精度
getcontext().prec = 1000

def fibonacci_decimal(n):
    phi = Decimal((1 + Decimal(5).sqrt()) / 2)
    psi = -1 / phi
    sqrt5 = Decimal(5).sqrt()
    return int((phi**n - psi**n) / sqrt5 + Decimal(0.5))  # 使用Decimal(0.5)来优化四舍五入

def fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# def check_fibonacci_accuracy(n):
#     fib_dp = fibonacci_dp(n)
#     fib_decimal = fibonacci_decimal(n)
#     if fib_dp == fib_decimal:
#         pass
#         # print(f"n={n}: DP and Decimal results match: {fib_dp}")
#     else:
#         print(f"n={n}: Mismatch! DP={fib_dp}, Decimal={fib_decimal}")
#         raise

# # 测试几个不同的n值
# for n in range(0,4767):  # 从0到49
#     check_fibonacci_accuracy(n)

import time
from memory_profiler import memory_usage

def profile_function(func, n):
    start_time = time.time()
    mem_usage = memory_usage((func, (n,)), interval=0.1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    max_memory = max(mem_usage) - min(mem_usage)
    return elapsed_time, max_memory

if __name__ == '__main__':
    n = 1000
    time_dp, mem_dp = profile_function(fibonacci_dp, n)
    time_decimal, mem_decimal = profile_function(fibonacci_decimal, n)

    print(f"Dynamic Programming: Time = {time_dp} seconds, Memory = {mem_dp} MiB")
    print(f"Decimal Formula: Time = {time_decimal} seconds, Memory = {mem_decimal} MiB")

