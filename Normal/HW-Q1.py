from collections import deque


def max_candies(grid, start, end):
    N = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start[0], start[1], 0, 0)])
    visited = set()
    visited.add((start[0], start[1]))

    min_step = float('inf')
    max_candies = 0

    while queue:
        x, y, step, candies = queue.popleft()

        if (x, y) == (end[0], end[1]):
            if step < min_step:
                max_candies = candies
                min_step = step
            elif step == min_step:
                max_candies = max(max_candies, candies)
            continue

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[nx][ny] != -1:
                visited.add((nx, ny))
                queue.append((nx, ny, step+1, candies + max(0, grid[nx][ny])))

    return max_candies


# 读取输入
def main():
    N = int(input())
    grid = []
    start = None
    end = None

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == -3:
                start = (i, j)
                row[j] = 0
            if row[j] == -2:
                end = (i, j)
                row[j] = 0
        grid.append(row)

    result = max_candies(grid, start, end)
    print(result)


if __name__ == "__main__":
    main()
