def get_result(a, b, v):
    n = len(a)

    # 预计算每个位置的 |A[i] - B[i]| 之差的绝对值
    diff = [abs(ord(a[i]) - ord(b[i])) for i in range(n)]

    max_length = 0
    current_sum = 0
    start = 0

    # 使用滑动窗口方法
    for end in range(n):
        current_sum += diff[end]

        # 当当前窗口的和大于V时，缩小窗口
        while current_sum > v:
            current_sum -= diff[start]
            start += 1

        # 更新最大长度
        max_length = max(max_length, end - start + 1)

    return max_length

if __name__ == "__main__":
    data = input().strip().split()
    a = data[0]
    b = data[1]
    v = int(data[2])

    print(get_result(a, b, v))
