from collections import deque

class Pos:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

def print_path(node):
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    path.reverse()
    for x, y in path:
        print(f"({x},{y})")

def find_path(maze, n, m):
    queue = deque()
    maze[0][0] = 2
    queue.append(Pos(0, 0, None))

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur = queue.popleft()
        
        for offsetX, offsetY in offsets:
            newX, newY = cur.x + offsetX, cur.y + offsetY

            if 0 <= newX < n and 0 <= newY < m and maze[newX][newY] == 0:
                maze[newX][newY] = 2
                next_pos = Pos(newX, newY, cur)
                queue.append(next_pos)

                if newX == n - 1 and newY == m - 1:
                    print_path(next_pos)
                    return

def main():

    n = int(input())
    m = int(input())
    maze = []
    for i in range(n):
            maze.append(list(map(int,input().split())))

    find_path(maze, n, m)

if __name__ == "__main__":
    main()
