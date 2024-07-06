import heapq

def main():
    data = input().split()
    
    t = int(data[0])
    n = int(data[1])
    
    road_cost = list(map(int, data[2:2 + n + 1]))
    mds = [list(map(int, data[2 + n + 1 + 2*i:2 + n + 1 + 2*i + 2])) for i in range(n)]
    
    total_road_cost = sum(road_cost)
    remain_days = t - total_road_cost
    
    if remain_days <= 0:
        print(0)
        return
    
    max_profit = []
    heapq.heapify(max_profit)
    
    for m, d in mds:
        day_profit = m
        while day_profit > 0:
            if len(max_profit) >= remain_days:
                if day_profit > max_profit[0]:
                    heapq.heappop(max_profit)
                else:
                    break
            heapq.heappush(max_profit, day_profit)
            day_profit -= d
    
    print(sum(max_profit))

if __name__ == "__main__":
    main()
