def climb(heights, strenght, idxs, direction):
    start = 0
    while heights[start] != 0 and start < len(heights):
        start += 1

    cost = 0
    for i in range(start + 1, len(heights)):
        if heights[i] == 0:
            cost = 0
            continue

        diff = heights[i] - heights[i - 1]

        if diff > 0:
            cost += diff * 3

            if i + 1 >= len(heights) or heights[i] > heights[i + 1]:
                if cost < strenght:
                    if direction:
                        idxs.add(i)
                    else:
                        idxs.add(len(heights)-1-i)
        
        elif diff < 0:
            cost -= diff * 3

def get_result(heights, strenght):
    idxs = set()
    climb(heigths, strenght, idxs, True)
    climb(heights[::-1], strenght, idxs, False)
    return len(idxs)


if __name__ == "__main__":
    heigths = list(map(int, input().strip().split()))
    strength = int(input())
    print(get_result(heigths, strength))
