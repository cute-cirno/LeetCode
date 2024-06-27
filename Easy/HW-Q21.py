def sumOfLeft(nums, jump, left):
    if left >= len(nums):
        return sum(nums)
    
    index = 0
    while len(nums) > left:
        # 计算命中点的索引
        index = (index + jump) % len(nums)
        # 移除命中点的元素
        nums.pop(index)
        print(nums)
    
    print(nums)
    return sum(nums)

# 测试用例
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jump = 2
left = 5
print("Sum of left:", sumOfLeft(nums, jump, left))  # 示例输出
