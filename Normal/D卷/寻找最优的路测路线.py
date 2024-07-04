import sys
import heapq

def main():
    r = int(input())
    c = int(input())
    
    matrix = [list(map(int, input().split())) for i in range(r)]

    # 初始化距离数组
    dist = [-float('inf')] * (r * c)
    dist[0] = matrix[0][0]

    # 使用优先队列（最大堆），存储的值取负以实现最大堆
    pq = [(-matrix[0][0], 0)]

    # 定义四个方向的偏移量
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current_value, u = heapq.heappop(pq)
        current_value = -current_value  # 恢复原始值

        y = u % c
        x = u // c

        if x == r - 1 and y == c - 1:
            break

        for offsetX, offsetY in offsets:
            newX = x + offsetX
            newY = y + offsetY

            if newX < 0 or newX >= r or newY < 0 or newY >= c:
                continue

            v = newX * c + newY
            w = min(current_value, matrix[newX][newY])

            if dist[v] < w:
                dist[v] = w
                heapq.heappush(pq, (-w, v))

    print(dist[r * c - 1])

if __name__ == "__main__":
    main()
