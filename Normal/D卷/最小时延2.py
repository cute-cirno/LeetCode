import collections

def spfa(matrix, dist, m, n):
    queue = collections.deque([(0, 0)])
    dist[0][0] = matrix[0][0]
    
    offsets = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    while queue:
        x, y = queue.popleft()

        for offsetX, offsetY in offsets:
            newX, newY = x + offsetX, y + offsetY

            if 0 <= newX < m and 0 <= newY < n:
                newDist = dist[x][y] + matrix[newX][newY]

                if matrix[newX][newY] == matrix[x][y] and matrix[x][y] >= 1:
                    newDist -= 1

                if newDist < dist[newX][newY]:
                    dist[newX][newY] = newDist
                    queue.append((newX, newY))

    return dist[m - 1][n - 1]

if __name__ == "__main__":
    data = input().strip().split()
    
    m = int(data[0])
    n = int(data[1])
    
    matrix = []
    idx = 2
    for i in range(m):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
        idx += n
    
    dist = [[float('inf')] * n for _ in range(m)]
    
    result = spfa(matrix, dist, m, n)
    print(result)
