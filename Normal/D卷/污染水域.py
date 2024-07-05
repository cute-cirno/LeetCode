
from collections import deque

def get_result(nums):
    n = int(len(nums) ** 0.5)
    total = len(nums)
    matrix = [[0] * n for _ in range(n)]
    queue = deque()

    index = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = nums[index]
            if matrix[i][j] == 1:
                queue.append((i, j))
                total -= 1
            index += 1

    if len(queue) == 0 or len(queue) == len(nums):
        return -1

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    day = 0

    while queue and total > 0:
        new_queue = deque()

        while queue:
            i, j = queue.popleft()
            for offset_i, offset_j in offsets:
                new_i = i + offset_i
                new_j = j + offset_j
                if 0 <= new_i < n and 0 <= new_j < n and matrix[new_i][new_j] == 0:
                    matrix[new_i][new_j] = 1
                    new_queue.append((new_i, new_j))
                    total -= 1

        queue = new_queue
        day += 1

    return day

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    result = get_result(nums)
    print(result)
