def find_min_k(x, y, cntx, cnty):
    def check(k):
        A = k // x
        B = k // y
        C = k // (x * y)
        return (
            max(0, cntx - (B - C)) + max(0, cnty - (A - C)) <= k - A - B + C
        )

    min_k = cntx + cnty
    max_k = 2 * min_k
    while min_k < max_k:
        mid_k = (min_k + max_k) // 2
        if check(mid_k):
            max_k = mid_k
        else:
            min_k = mid_k + 1

    return min_k

if __name__ == "__main__":
    x, y, cntx, cnty = map(int, input().strip().split())
    result = find_min_k(x, y, cntx, cnty)
    print(result)
