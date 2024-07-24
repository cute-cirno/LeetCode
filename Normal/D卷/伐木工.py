

class Timber:
    def __init__(self, max_profit, optimal_cuts):
        self.max_profit = max_profit
        self.optimal_cuts = optimal_cuts

def main():
    timber_length = int(input().strip())  # 读取输入数据

    # 创建动态规划数组，用于存储每个长度的木材的最大收益和最优切割方案
    dp = [Timber(length, [length]) for length in range(timber_length + 1)]

    # 从长度为2的木材开始，尝试所有可能的切割方式
    for length in range(2, timber_length + 1):
        for cut in range(1, length):
            current_profit = dp[cut].max_profit * dp[length - cut].max_profit

            # 如果找到了一个更优的切割方案，则更新最大收益和最优切割方案
            if current_profit > dp[length].max_profit or \
               (current_profit == dp[length].max_profit and \
                len(dp[length].optimal_cuts) > len(dp[cut].optimal_cuts) + len(dp[length - cut].optimal_cuts)):
                dp[length].max_profit = current_profit
                dp[length].optimal_cuts = dp[cut].optimal_cuts + dp[length - cut].optimal_cuts

    # 对最优切割方案进行升序排序，并按照题目要求输出
    result = ' '.join(map(str, sorted(dp[timber_length].optimal_cuts)))

    # 打印切割方案
    print(result)

if __name__ == "__main__":
    main()


l = int(input().strip())

if l // 3 == 0:
    cuts = [l]
else:
    num = l % 3
    if num == 0:
        cuts = [3 for i in range(l//3)]
    elif num == 1:
        cuts = [3 for i in range(l//3)]
        cuts[-1] += 1
    else:
        cuts = [2]
        for i in range(l//3):
            cuts.append(3)

print(' '.join(map(str, cuts)))