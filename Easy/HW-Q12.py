def min_string_by_one_swap(s):
    # 对字符串s进行排序，得到字典序最小的字符串
    t = ''.join(sorted(s))
    n = len(s)
    
    # 查找第一个不同的字符位置
    for i in range(n):
        if s[i] != t[i]:
            # 找到第一个使得s和t不同的位置i后，找到对应的最小字符在原字符串中的位置j
            j = s.rfind(t[i])  # 从后向前找到t[i]的位置，确保是最远的位置
            # 交换s中的i和j位置的字符
            s = list(s)
            s[i], s[j] = s[j], s[i]
            s = ''.join(s)
            break
    
    return s

# 示例使用
input_str = "bbcdaa"
print("Original string:", input_str)
print("Minimum string after one swap:", min_string_by_one_swap(input_str))
