import sys

def solution(nums):
    if any(num < 1 or num > 9 for num in nums):
        return -1

    num_set = set(nums)
    if len(num_set) != 4:
        return -1

    if 2 in num_set and 5 in num_set:
        return -1

    if 6 in num_set and 9 in num_set:
        return -1

    path = []
    vis = [False] * len(nums)
    map_replacements = {2: 5, 5: 2, 6: 9, 9: 6}
    res = []

    def dfs(nums, vis, path, map_replacements, res):
        if path:
            res.append(int(''.join(map(str, path))))

        if len(path) == len(nums):
            return

        for i in range(len(nums)):
            if vis[i]:
                continue

            vis[i] = True
            path.append(nums[i])
            dfs(nums, vis, path, map_replacements, res)
            path.pop()

            if nums[i] in map_replacements and not vis[nums.index(map_replacements[nums[i]])]:
                path.append(map_replacements[nums[i]])
                dfs(nums, vis, path, map_replacements, res)
                path.pop()

            vis[i] = False

    dfs(nums, vis, path, map_replacements, res)
    res.sort()

    n = min(max(nums), len(res))
    return res[n - 1] if n > 0 else -1

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    nums = list(map(int, input_data.split(",")))
    print(solution(nums))
