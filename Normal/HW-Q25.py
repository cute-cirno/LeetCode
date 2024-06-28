def dfs(grid, visited, x, y):
    n, m = len(grid), len(grid[0])
    stack = [(x, y)]
    count = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        count += 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                stack.append((nx, ny))

    return count

def largest_lan(grid):
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_lan_size = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                max_lan_size = max(max_lan_size, dfs(grid, visited, i, j))

    return max_lan_size

# 输入处理
n, m = map(int, input().strip().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))

# 输出结果
print(largest_lan(grid))
