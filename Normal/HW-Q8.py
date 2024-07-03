from math import factorial
from collections import Counter

def count_ways(n, m):
    way_set = set()
    def distribute(n, m, current_distribution,last_num):
        if n == 0 and m > 0:
            return
        if m == 1:
            current_distribution.append(n)
            valid_distribution(current_distribution)
            return

        for i in range(last_num, n//m+1):
            distribute(n - i, m - 1, current_distribution + [i],i)

    def valid_distribution(distribution):
        if len(distribution) < 2:
            way_set.add(tuple(distribution))
            return
        for i in range(len(distribution) - 1):
            if abs(distribution[i+1] - distribution[i]) > 3:
                return
        way_set.add(tuple(distribution))
        
    # def count_permutations(t):
    #     counter = Counter(t)
    #     numerator = factorial(len(t))
    #     denominator = 1
    #     for count in counter.values():
    #         denominator *= factorial(count)
    #     return numerator // denominator
        
    distribute(n, m, [],1)
    return len(way_set)
    # return sum([count_permutations(_) for _ in way_set])

# 示例用法
n = 8  # 月饼数量
m = 3  # 员工数量

total_ways = count_ways(n, m)
print(f"总分配方法数: {total_ways}")
