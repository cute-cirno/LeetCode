
from collections import deque
data = input().split()
m, n = int(data[0]), int(data[1])
map_data = data[2:]

reach = set()
map_matrix = []
step_map = [[0] * n for _ in range(m)]
offsets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

for i in range(m):
    map_matrix.append(map_data[i])
    for j in range(n):
        reach.add(i * n + j)

def is_valid(x, y):
    return 0 <= x < m and 0 <= y < n

def get_new_pos(x, y, offset_x, offset_y):
    return x + offset_x, y + offset_y

def bfs(sx, sy, k):
    queue = deque([(sx, sy, 0)])
    vis = set()
    vis.add(sx * n + sy)

    while queue and k > 0:
        new_queue = deque()
        for x, y, step in queue:
            for offset_x, offset_y in offsets:
                new_x, new_y = get_new_pos(x, y, offset_x, offset_y)
                pos = new_x * n + new_y
                if not is_valid(new_x, new_y) or pos in vis:
                    continue
                new_queue.append((new_x, new_y, step + 1))
                step_map[new_x][new_y] += step + 1
                vis.add(pos)
        queue = new_queue
        k -= 1

def get_result():
    for i in range(m):
        for j in range(n):
            if map_matrix[i][j] != ".":
                k = int(map_matrix[i][j])
                bfs(i, j, k)

    if not reach:
        return -1

    min_step = float('inf')
    for pos in reach:
        y = pos % n
        x = (pos - y) // n
        min_step = min(min_step, step_map[x][y])
    return min_step

print(get_result())
