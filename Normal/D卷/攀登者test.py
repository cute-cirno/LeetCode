def climb(heights, strength, idxs, direction):
    start = 0
    while start < len(heights) and heights[start] != 0:
        start += 1

    cost = 0
    for i in range(start + 1, len(heights)):
        if heights[i] == 0:
            cost = 0
            continue

        diff = heights[i] - heights[i - 1]

        if diff > 0:
            cost += 3 * diff

            if i + 1 >= len(heights) or heights[i] > heights[i + 1]:
                if cost < strength:
                    if direction:
                        idxs.add(i)
                    else:
                        idxs.add(len(heights) - 1 - i)
        elif diff < 0:
            cost -= diff * 3


def get_result():
    idxs = set()
    climb(heights, strength, idxs, True)
    climb(heights[::-1], strength, idxs, False)
    return len(idxs)


if __name__ == "__main__":
    heights = list(map(int, input().strip().split()))
    strength = int(input())
    print(get_result(heights, strength))
