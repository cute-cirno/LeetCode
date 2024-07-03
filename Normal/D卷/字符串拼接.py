def get_result(s, n):
    # 如果字符串长度小于 n，则无法形成长度为 n 的子序列
    if len(s) < n:
        return 0

    # 检查字符串中是否有非小写字母的字符，如果有则返回 0
    for c in s:
        if c < 'a' or c > 'z':
            return 0

    # 将字符串排序并转换为字符数组
    c_arr = sorted(s)
    
    # 调用 dfs 函数进行深度优先搜索，计算满足条件的子序列数量
    return dfs(c_arr, -1, 0, [False] * len(c_arr), n, 0)

def dfs(c_arr, pre, level, used, n, count):
    # 如果当前递归深度等于 n，说明已经形成一个长度为 n 的子序列
    if level == n:
        return count + 1

    # 遍历字符数组中的每个字符
    for i in range(len(c_arr)):
        # 如果字符已经被使用，则跳过
        if used[i]:
            continue
        # 如果当前字符与上一个字符相同，则跳过，避免重复计算
        if pre >= 0 and c_arr[i] == c_arr[pre]:
            continue
        # 如果当前字符与前一个字符相同，并且前一个字符未被使用，则跳过，避免重复计算
        if i > 0 and c_arr[i] == c_arr[i - 1] and not used[i - 1]:
            continue

        # 标记当前字符为已使用
        used[i] = True
        # 递归调用 dfs 函数，继续形成子序列
        count = dfs(c_arr, i, level + 1, used, n, count)
        # 回溯，将当前字符标记为未使用
        used[i] = False

    return count

if __name__ == "__main__":
    data = input().strip().split()
    
    s = data[0]
    n = int(data[1])
    
    print(get_result(s, n))
