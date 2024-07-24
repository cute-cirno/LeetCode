def max_profit(weightA, weightB, truckCapacity, priceA, priceB):
    # 初始化最大利润为0
    maxProfit = 0

    # 遍历每可能的数量 A 从 1 开始，确保货车至少装有一件 A 和一件 B
    for quantityA in range(1, (truckCapacity // weightA) + 1):
        remainingCapacity = truckCapacity - weightA * quantityA
        if remainingCapacity >= weightB:  # 确保至少有空间装一件 B
            if remainingCapacity % weightB == 0:
                quantityB = remainingCapacity // weightB
                # 计算当前配置的利润
                currentProfit = quantityA * priceA + quantityB * priceB
                # 更新最大利润
                maxProfit = max(maxProfit, currentProfit)

    return maxProfit

# 输入处理
data = input().strip().split()
weightA, weightB, truckCapacity, priceA, priceB = map(int, data)

# 输出最大利润
print(max_profit(weightA, weightB, truckCapacity, priceA, priceB))
