import sys
from collections import deque

def get_result(n, scores, k):
    k += 1

    dp = [0] * n
    dp[0] = scores[0]

    queue = deque()
    queue.append(dp[0])

    for i in range(1, min(k, n)):
        dp[i] = queue[0] + scores[i]

        while queue and dp[i] > queue[-1]:
            queue.pop()

        queue.append(dp[i])

    for i in range(k, n):
        if dp[i - k] == queue[0]:
            queue.popleft()

        dp[i] = queue[0] + scores[i]

        while queue and dp[i] > queue[-1]:
            queue.pop()

        queue.append(dp[i])

    return dp[-1]

def main():
    data = input().strip().split()
    n = int(data[0])
    scores = list(map(int, data[1:n+1]))
    k = int(data[n+1])

    result = get_result(n, scores, k)
    print(result)

if __name__ == "__main__":
    main()
