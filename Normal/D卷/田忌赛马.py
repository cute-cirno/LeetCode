def main():
    data = input().split()
    a = list(map(int, data[:len(data)//2]))
    b = list(map(int, data[len(data)//2:]))

    max_bigger_count = 0
    ans = 0

    def dfs(level, used, bigger_count):
        nonlocal max_bigger_count, ans
        if level >= len(a):
            if bigger_count > max_bigger_count:
                max_bigger_count = bigger_count
                ans = 1
            elif bigger_count == max_bigger_count:
                ans += 1
        else:
            for i in range(len(a)):
                if not used[i]:
                    used[i] = True
                    dfs(level + 1, used, bigger_count + (a[i] > b[level]))
                    used[i] = False

    dfs(0, [False] * len(a), 0)
    print(ans)

if __name__ == "__main__":
    main()
