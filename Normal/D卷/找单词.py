def find_letter(grid, n, str):
    def dfs(i, j, k, path):
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != str[k] or visited[i][j]:
            return False
        
        path.append((i, j))
        visited[i][j] = True

        if k == len(str) - 1:
            return True

        # 递归搜索相邻的四个方向
        if (dfs(i - 1, j, k + 1, path) or 
            dfs(i + 1, j, k + 1, path) or
            dfs(i, j - 1, k + 1, path) or
            dfs(i, j + 1, k + 1, path)):
            return True
        
        # 如果没有找到匹配，回溯
        path.pop()
        visited[i][j] = False
        return False

    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str[0]:
                path = []
                if dfs(i, j, 0, path):
                    return ",".join([f"{x},{y}" for x, y in path])
    return "N"

if __name__ == "__main__":
    n = int(input())
    grid= []
    for _ in range(n):
        grid.append(input().split(','))
    str_to_find = input().strip()
    
    result = find_letter(grid, n, str_to_find)
    print(result)
