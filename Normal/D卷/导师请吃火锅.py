def max_dishes(n, m, dishes):
    # 将菜按照刚好合适的时间排序
    dishes.sort(key=lambda dish: dish[0] + dish[1])
    
    # 初始化
    current_time = 0
    count = 0
    
    for dish in dishes:
        ready_time = dish[0] + dish[1]
        if ready_time > current_time:
            count += 1
            current_time = ready_time + m
    
    return count

# 读取输入
if __name__ == "__main__":
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    dishes = []
    for i in range(n):
        x = int(data[2 + i * 2])
        y = int(data[3 + i * 2])
        dishes.append((x, y))
    
    # 计算结果
    result = max_dishes(n, m, dishes)
    
    # 输出结果
    print(result)
