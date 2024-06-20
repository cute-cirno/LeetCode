def find_consecutive_sums(N):
    count = 0
    for k in range(1, N+1):
        # Calculate the term to check if it is divisible by k
        term = N - k * (k - 1) // 2
        if term <= 0:
            break
        if term % k == 0:
            a = term // k
            if a > 0:
                count += 1
                print(f"序列 {count}: ", end="")
                print(" + ".join(str(a + i) for i in range(k)) + f" = {N}")
    print(f"总共有 {count} 种表示方法。")

# Example
N = 15
find_consecutive_sums(N)
