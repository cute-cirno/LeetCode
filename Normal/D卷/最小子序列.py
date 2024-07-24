def smallestSubsequence(s):
    # 记录每个字符的剩余数量
    count = {c: 0 for c in set(s)}
    for c in s:
        count[c] += 1
    
    # 结果栈
    result = []
    # 已经加入栈中的字符集合，用于快速检查是否重复
    in_stack = set()
    
    for c in s:
        # 当前字符计数减一
        count[c] -= 1
        
        # 如果字符已经在结果中，跳过
        if c in in_stack:
            continue
        
        # 保证字典序最小且字符不重复
        while result and result[-1] > c and count[result[-1]] > 0:
            in_stack.remove(result.pop())
        
        # 将当前字符加入栈，并加入到集合中
        result.append(c)
        in_stack.add(c)
    
    # 将结果列表转换为字符串输出
    return ''.join(result)

# 示例
# print(smallestSubsequence("bcabc"))  # 输出: "abc"
print(smallestSubsequence("czacdczcddaaacasfasfa"))  # 输出: "acdb"
