def divide_mooncake(m, n):
    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    
    # 初始化dp表，只有一个员工时的情况
    for k in range(1, n + 1):
        dp[1][k][k] = 1

    # 填充dp表
    for i in range(2, m + 1):
        for j in range(i, n + 1):
            for k in range(1, j):
                for l in range(max(1, k - 3), k + 1):
                    dp[i][j][k] += dp[i - 1][j - k][l]

    # 计算总的分配方案数
    ans = sum(dp[m][n][i] for i in range(1, n + 1))
    return ans

if __name__ == "__main__":
    m = 2
    n = 4
    result = divide_mooncake(m, n)
    print(result)
