import heapq

def calcTime(lights, timePerRoad, rowStart, colStart, rowEnd, colEnd):
    n = len(lights)
    m = len(lights[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def get_wait_time(current_time, light_cycle):
        if light_cycle == 0:
            return 0
        return (light_cycle - current_time % light_cycle) % light_cycle

    pq = [(0, rowStart, colStart)]
    min_time = [[float('inf')] * m for _ in range(n)]
    min_time[rowStart][colStart] = 0

    while pq:
        current_time, x, y = heapq.heappop(pq)
        
        if (x, y) == (rowEnd, colEnd):
            return current_time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny):
                if dx == 0 or dy == 0:  # straight or left turn, need to wait for light
                    wait_time = get_wait_time(current_time, lights[nx][ny])
                    new_time = current_time + timePerRoad + wait_time
                else:  # right turn, no need to wait for light
                    new_time = current_time + timePerRoad
                
                if new_time < min_time[nx][ny]:
                    min_time[nx][ny] = new_time
                    heapq.heappush(pq, (new_time, nx, ny))

    return -1

def main():
    data = input().split()
    
    index = 0
    
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    
    lights = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[index]))
            index += 1
        lights.append(row)
    
    timePerRoad = int(data[index])
    index += 1
    
    rowStart = int(data[index])
    index += 1
    colStart = int(data[index])
    index += 1
    
    rowEnd = int(data[index])
    index += 1
    colEnd = int(data[index])
    
    result = calcTime(lights, timePerRoad, rowStart, colStart, rowEnd, colEnd)
    print(result)

if __name__ == "__main__":
    main()
