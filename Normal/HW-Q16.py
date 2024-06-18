def max_bananas(numbers, N):
    n = len(numbers)
    if N >= n:
        return sum(numbers)
    
    # 计算前缀和数组
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + numbers[i - 1]
    
    print(prefix_sums)
    max_bananas = 0
    
    # 考虑所有可能的k值（从头部取的数量）
    for k in range(N + 1):
        # 从头部取k个香蕉
        head = prefix_sums[min(k, n)]  # 防止k超出数组长度
        
        # 从尾部取N-k个香蕉
        tail = 0
        if N - k <= n and N - k > 0:  # 确保从尾部取的数量有效
            tail = prefix_sums[n] - prefix_sums[n - (N - k)]
        
        # 计算当前组合的总香蕉数并更新最大值
        max_bananas = max(max_bananas, head + tail)
    
    return max_bananas

# 示例
numbers = [1, 13, 11, 4, 5, 7, 1, 1, 1,1,1,1,12,12,1]
N = 5
print(max_bananas(numbers, N))  # 输出最大可能的香蕉数
