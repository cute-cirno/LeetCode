from heapq import heappush, heappop

def is_right_turn(prev_direction, new_direction):
    # 使用向量叉乘来确定转向类型，右转的叉乘结果为负
    return prev_direction[0] * new_direction[1] - prev_direction[1] * new_direction[0] == 1

def calcTime(lights, timePerRoad, rowStart, colStart, rowEnd, colEnd):
    n = len(lights)
    m = len(lights[0])
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 右, 下, 左, 上
    priority_queue = []
    heappush(priority_queue, (0, rowStart, colStart, None))  # (accumulated_time, row, col, last_direction)
    min_time = {(rowStart, colStart): 0}
    parents = {(rowStart, colStart): None}  # To track the path

    while priority_queue:
        acc_time, row, col, last_dir = heappop(priority_queue)
        
        if row == rowEnd and col == colEnd:
            path = []
            step = (row, col)
            while step:
                path.append(step)
                step = parents[step]
            return acc_time, path[::-1]  # Return time and path reversed to start from the beginning
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_dir = (dr, dc)
            if 0 <= new_row < n and 0 <= new_col < m:
                additional_time = timePerRoad
                if last_dir is not None and not is_right_turn(last_dir, new_dir):
                    additional_time += lights[row][col]
                new_time = acc_time + additional_time
                
                if (new_row, new_col) not in min_time or new_time < min_time[(new_row, new_col)]:
                    min_time[(new_row, new_col)] = new_time
                    heappush(priority_queue, (new_time, new_row, new_col, new_dir))
                    parents[(new_row, new_col)] = (row, col)  # Record the path
    
    return -1, []  # If no path found

# 测试用例
lights = [
    [30, 20, 0],
    [10, 60, 40],
    [40, 25, 20]
]
time, path = calcTime(lights, 5, 0, 0, 2, 2)
print("Minimum time:", time)
print("Path:", path)
