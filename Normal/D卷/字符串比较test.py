def get_result(a, b, v):
    n = len(a)

    diff = [abs(ord(a[i]) - ord(b[i])) for i in range(n)]
    
    max_length = 0
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += diff[end]

        while current_sum > v:
            current_sum -= diff[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


if __name__ == "__main__":
    a, b, v = input().strip().split()
    v = int(v)

    print(get_result(a, b, v))
