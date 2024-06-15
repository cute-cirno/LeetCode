from itertools import permutations


def max_greater_pairs_count(a, b):
    a.sort()
    b.sort()

    i = len(a) - 1
    j = len(b) - 1
    count = 0

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            count += 1
            i -= 1
            j -= 1
        else:
            j -= 1

    return count


def count_optimal_permutations(a, b):
    optimal_count = max_greater_pairs_count(a, b)
    count = 0
    for perm in permutations(a):
        if max_greater_pairs_count(list(perm), b) == optimal_count:
            count += 1
    return count


a = [1, 2, 3]
b = [4, 5, 6]
print(count_optimal_permutations(a, b))  # 应该输出 6


a = [8, 1, 7, 3, 6, 1, 4, 6, 11,17]
b = [4, 10, 2, 5, 9, 245, 343, 12, 3,1]
print(count_optimal_permutations(a, b))  # 输出所有可以达到最优结果的a数组数量
