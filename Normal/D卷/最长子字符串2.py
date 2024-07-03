def get_result(s):
    status = 0b000

    # 初始化map
    map = [[] for _ in range(8)]
    map[0].append(-1)

    max_len = 0

    for i in range(len(s) * 2):
        c = s[i % len(s)]

        if c == "l":
            status ^= 0b100
        elif c == "o":
            status ^= 0b010
        elif c == "x":
            status ^= 0b001

        if i < len(s):
            map[status].append(i)

        while len(map[status]) > 0:
            earliest = map[status][0]

            if i - earliest > len(s):
                map[status].pop(0)
            else:
                max_len = max(max_len, i - earliest)
                break

    return max_len

if __name__ == "__main__":
    data = input().strip()

    print(get_result(data))
