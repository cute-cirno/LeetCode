def min_delivery_time(delivery_persons, community_count, times):
    def can_deliver(max_time):
        count = 1
        current_sum = 0
        for time in times:
            if current_sum + time > max_time:
                count += 1
                current_sum = time
                if count > delivery_persons:
                    return False
            else:
                current_sum += time
        return True

    left, right = max(times), sum(times)
    while left < right:
        mid = (left + right) // 2
        if can_deliver(mid):
            right = mid
        else:
            left = mid + 1
    return left


delivery_persons = int(input())
community_count = int(input())
times = list(map(int, input().split()))

result = min_delivery_time(delivery_persons, community_count, times)
print(result)
