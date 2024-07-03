from collections import deque

offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]


class Node:
    def __init__(self, x, y, init, remain, flag):
        self.x = x
        self.y = y
        self.init = init
        self.remain = remain
        self.flag = flag


def bfs(matrix, m, n):
    if matrix[0][0] == 0 or matrix[m - 1][n - 1] == 0:
        return -1

    queue = deque()

    if matrix[0][0] == -1:
        src = Node(0, 0, 0, 100, True)
    else:
        src = Node(0, 0, matrix[0][0], 0, False)

    queue.append(src)

    dist_init = [[float("inf")] * n for _ in range(m)]
    dist_remain = [[0] * n for _ in range(m)]

    dist_init[0][0] = src.init
    dist_remain[0][0] = src.remain

    while queue:
        cur = queue.popleft()

        for offset in offsets:
            newX, newY = cur.x + offset[0], cur.y + offset[1]

            if newX < 0 or newX >= m or newY < 0 or newY >= n or matrix[newX][newY] == 0:
                continue

            init = cur.init
            remain = cur.remain
            flag = cur.flag

            if matrix[newX][newY] == -1:
                remain = 100
                flag = True
            else:
                remain -= matrix[newX][newY]

            if remain < 0:
                if flag:
                    continue
                else:
                    init -= remain
                    remain = 0

            if init > 100:
                continue

            if init < dist_init[newX][newY] or remain > dist_remain[newX][newY]:
                dist_init[newX][newY] = init
                dist_remain[newX][newY] = remain

                next_node = Node(newX, newY, init, remain, flag)
                queue.append(next_node)
    return dist_init[m - 1][n - 1] if dist_init[m - 1][n - 1] != float("inf") else -1


if __name__ == "__main__":
    m, n = list(map(int, input().strip().split()))
    matrix = []

    for i in range(m):
        row = list(map(int, input().strip().split()))
        matrix.append(row)

    result = bfs(matrix, m, n)
    print(result)
