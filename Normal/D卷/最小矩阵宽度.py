import sys
from collections import defaultdict

def get_result(matrix, n, m, k, nums):
    cnts = defaultdict(int)
    for num in nums:
        cnts[num] += 1
    
    total = k
    min_len = float('inf')
    l = 0
    r = 0

    while r < m:
        for i in range(n):
            num = matrix[i][r]
            if cnts[num] > 0:
                total -= 1
            cnts[num] -= 1

        while total == 0:
            min_len = min(min_len, r - l + 1)
            for i in range(n):
                num = matrix[i][l]
                cnts[num] += 1
                if cnts[num] > 0:
                    total += 1
            l += 1

        r += 1

    return -1 if min_len == float('inf') else min_len

if __name__ == "__main__":
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
        index += m
    
    k = int(input())
    nums = list(map(int, input().strip().split()))
    
    result = get_result(matrix, n, m, k, nums)
    print(result)
