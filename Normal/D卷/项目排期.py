import heapq

def get_min_completion_time(workloads, n):
    # 将需求工作量从大到小排序
    workloads.sort(reverse=True)
    
    # 初始化最小堆，将每个开发人员的初始工作量设置为0
    min_heap = [0] * n
    heapq.heapify(min_heap)
    
    # 遍历排序后的需求工作量
    for workload in workloads:
        # 将当前需求分配给工作量最小的开发人员
        min_load = heapq.heappop(min_heap)
        min_load += workload
        heapq.heappush(min_heap, min_load)
    
    # 堆顶的元素即为完成所有工作的最短时间
    print(min_heap)
    return max(min_heap)

if __name__ == "__main__":
    # 输入处理
    workloads = list(map(int, input().strip().split()))
    n = int(input().strip())
    
    # 获取最短完成时间
    result = get_min_completion_time(workloads, n)
    
    # 输出结果
    print(result)
