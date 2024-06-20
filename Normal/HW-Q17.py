def next_higher_same_bit_count(n):
    c = n & -n
    r = n + c
    ones = n ^ r
    ones = (ones // c) >> 2
    return r | ones

n = 128  # 10000000 in binary
m = next_higher_same_bit_count(n)
print(f"下一个比 {n} 大且二进制中 1 的个数相同的数是: {m}")
