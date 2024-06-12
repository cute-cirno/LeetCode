def findBiggerFriends(heights):
    n = len(heights)
    if n == 0:
        return []
    
    result = [0] * n  # 结果列表，初始化为0
    stack = []  # 栈，用于存储小朋友的索引

    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            index = stack.pop()
            result[index] = i + 1  # 存储的是位置，所以加1
        stack.append(i)
    
    return result

def main():
    N = int(input().strip())
    if N == 0:
        print("")
        return
    
    heights = list(map(int, input().strip().split()))
    
    if len(heights) != N:
        print("The number of heights provided does not match the number of children.")
        return

    friend_positions = findBiggerFriends(heights)
    
    print(' '.join(map(str, friend_positions)))

if __name__ == "__main__":
    main()
