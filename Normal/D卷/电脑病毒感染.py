def network_infection(n, edges, start):
    # 构建图的邻接表
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # 因为是无向图，双向添加
    
    # 初始化最小堆（优先队列）和距离字典
    min_heap = [(0, start)]
    dist = {i: float('inf') for i in range(n)}
    dist[start] = 0
    
    while min_heap:
        # 手动实现的堆（最小堆）pop操作
        min_heap.sort()
        current_dist, u = min_heap.pop(0)
        
        if current_dist > dist[u]:
            continue
        
        for v, w in graph[u]:
            distance = current_dist + w
            
            if distance < dist[v]:
                dist[v] = distance
                # 手动实现的堆（最小堆）push操作
                min_heap.append((distance, v))
    
    max_dist = max(dist.values())
    return -1 if max_dist == float('inf') else max_dist

# 读取输入
if __name__ == "__main__":
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    m = int(data[index])
    index += 1
    
    edges = []
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        w = int(data[index + 2])
        edges.append((u, v, w))
        index += 3
    
    start = int(data[index]) - 1
    
    result = network_infection(n, edges, start)
    
    print(result)
