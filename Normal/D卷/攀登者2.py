def climb(heights, strength, idxs, direction):
    j = 0
    while j < len(heights) and heights[j] != 0:
        j += 1

    cost = 0
    for i in range(j + 1, len(heights)):
        if heights[i] == 0:
            cost = 0
            continue

        diff = heights[i] - heights[i - 1]

        if diff > 0:
            cost += diff * 3

            if i + 1 >= len(heights) or heights[i] > heights[i + 1]:
                if cost < strength:
                    if direction:
                        idxs.add(i)
                    else:
                        idxs.add(len(heights) - i - 1)
        elif diff < 0:
            cost -= diff * 3


def get_result(heights, strength):
    idxs = set()
    climb(heights, strength, idxs, True)
    climb(heights[::-1], strength, idxs, False)
    return len(idxs)


if __name__ == "__main__":
    data = input().strip().split()
    heights = list(map(int, data[0].split(",")))
    strength = int(data[1])
    print(get_result(heights, strength))
