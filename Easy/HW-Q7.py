def is_subsequence(S, L):
    i, j = 0, 0
    while i < len(S) and j < len(L):
        if S[i] == L[j]:
            i += 1
        j += 1
    return i == len(S)

# 示例用法
S = "ace"
L = "abcde"

print(is_subsequence(S, L))  # 输出: True

S = "aec"
L = "abcde"

print(is_subsequence(S, L))  # 输出: False
