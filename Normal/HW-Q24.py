def count_teams(level):
    n = len(level)
    left_less = [0] * n
    left_greater = [0] * n
    right_less = [0] * n
    right_greater = [0] * n

    # Calculate left_less and left_greater
    for j in range(n):
        for i in range(j):
            if level[i] < level[j]:
                left_less[j] += 1
            elif level[i] > level[j]:
                left_greater[j] += 1

    # Calculate right_less and right_greater
    for j in range(n):
        for k in range(j + 1, n):
            if level[k] < level[j]:
                right_less[j] += 1
            elif level[k] > level[j]:
                right_greater[j] += 1

    count = 0
    # Calculate the number of valid teams
    for j in range(n):
        count += left_less[j] * right_greater[j]
        count += left_greater[j] * right_less[j]

    return count

# Example usage
level = [2, 5, 3, 4, 1]
print(count_teams(level))  # Output: 3
