def get_min_time(tasks, n):
    from collections import Counter
    import heapq

    task_counts = Counter(tasks)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    time = 0
    cooldown = []

    while max_heap or cooldown:
        time += 1
        if max_heap:
            count = heapq.heappop(max_heap) + 1  # Increase since it's a negative count in max_heap
            if count:
                cooldown.append((count, time + n))

        if cooldown and cooldown[0][1] == time:
            heapq.heappush(max_heap, cooldown.pop(0)[0])

    return time


# 读取输入
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    tasks = list(map(int, data[0].split(',')))
    n = int(data[1])
    
    result = get_min_time(tasks, n)
    print(result)
