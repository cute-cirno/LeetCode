def max_social_distance(seatNum, seatOrLeave):
    # 初始化一个集合来存储已占用的座位
    occupied = set()
    last_seat = -1  # 用于记录最后一个进来的员工所坐的座位

    for action in seatOrLeave:
        if action == 1:
            # 员工进场的情况
            if not occupied:
                # 如果没有任何座位被占用，第一个员工直接坐在座位0上
                occupied.add(0)
                last_seat = 0
            else:
                # 查找最佳座位
                max_distance = -1
                best_seat = -1
                occupied_list = sorted(occupied)
                
                # 检查第一个座位
                if occupied_list[0] != 0:
                    # 如果第一个座位未被占用，计算其社交距离
                    distance = occupied_list[0]
                    if distance > max_distance:
                        max_distance = distance
                        best_seat = 0
                
                # 检查已占用座位之间的空座位
                for i in range(1, len(occupied_list)):
                    prev_seat = occupied_list[i - 1]
                    next_seat = occupied_list[i]
                    # 计算当前空位的社交距离
                    distance = (next_seat - prev_seat) // 2
                    candidate = prev_seat + distance
                    # 更新最佳座位
                    if distance > max_distance or (distance == max_distance and candidate < best_seat):
                        max_distance = distance
                        best_seat = candidate
                
                # 检查最后一个座位
                if occupied_list[-1] != seatNum - 1:
                    # 如果最后一个座位未被占用，计算其社交距离
                    distance = seatNum - 1 - occupied_list[-1]
                    if distance > max_distance:
                        best_seat = occupied_list[-1] + distance
                
                # 更新已占用的座位和最后一个员工的位置
                occupied.add(best_seat)
                last_seat = best_seat
        else:
            # 员工离场的情况
            seat_to_leave = -action
            # 将离开的座位从已占用座位中移除
            occupied.remove(seat_to_leave)
    
    # 如果所有座位都已满，返回-1，否则返回最后一个进来的员工的位置
    return last_seat if len(occupied) < seatNum else -1

# 测试用例
seatNum = 10
seatOrLeave = [1, 1, 1, 1, 1, -4, 1]
print(max_social_distance(seatNum, seatOrLeave))  # 应该输出 4
