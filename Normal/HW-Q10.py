def longest_even_substring(s):
    n = len(s)
    s = s * 2  # 将字符串首尾相连
    max_length = 0
    prefix = {0: -1}  # 存储状态和其最早出现的索引
    state = 0
    
    for i in range(len(s)):
        if s[i] in 'lox':
            bit = {'l': 1, 'o': 2, 'x': 4}[s[i]]
            state ^= bit  # 更新状态

        if state in prefix:
            max_length = max(max_length, i - prefix[state])
        else:
            prefix[state] = i
    
    return min(max_length, n)  # 最长子字符串长度不能超过原始字符串长度

# 示例
s = "loxloxl"
print(longest_even_substring(s))  # 输出最长子字符串长度
