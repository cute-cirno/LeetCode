import sys

def main():
    # 读取 n 和 m
    n, m = map(int, input().split())
    
    # 读取矩阵
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    
    # 如果起点或终点是障碍物，直接返回 0
    if matrix[0][0] == 1 or matrix[n - 1][m - 1] == 1:
        print(0)
        return
    
    # 初始化 dp 数组
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    # 填充 dp 数组
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    
    # 输出结果
    print(dp[n - 1][m - 1])

if __name__ == "__main__":
    main()
