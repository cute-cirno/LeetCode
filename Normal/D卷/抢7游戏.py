def main():
    m = int(input().strip())

    factor = init_factor(m - 7)

    one_count = m - 7
    two_count = 0

    ans = 0

    while one_count >= 0:
        if (one_count + two_count) % 2 != 0:
            ans += get_permutation_count(one_count, two_count, factor)
        
        one_count -= 2
        two_count += 1

    print(ans)

def get_permutation_count(one_count, two_count, factor):
    if one_count == 0 or two_count == 0:
        return 1
    else:
        return factor[one_count + two_count] // (factor[one_count] * factor[two_count])

def init_factor(n):
    factor = [1] * (n + 1)

    for i in range(1, n + 1):
        factor[i] = i * factor[i - 1]

    return factor

if __name__ == "__main__":
    main()
