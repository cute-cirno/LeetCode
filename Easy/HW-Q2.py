def sum_max_min_n(arr, N):
    
    # 检查数组长度是否至少是 2N
    if len(arr) < 2*N:
        return -1
    
    # 去除重复元素
    arr = list(set(arr))

    # 将数组排序
    arr = sorted(arr)
    
    # 取最小N个数和最大N个数
    max_n = arr[:N]
    min_n = arr[-N:]    
    
    # 检查是否有重叠
    if set(max_n) & set(min_n):
        return -1
    
    # 计算和
    return sum(max_n) + sum(min_n)

# 测试
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
N = 3
print(sum_max_min_n(arr, N))  # 输出应为27（0+1+2+7+8+9）
