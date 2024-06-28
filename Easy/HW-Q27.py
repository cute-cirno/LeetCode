def quicksort(arr, key):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x) < key(pivot)]
    middle = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]

    return quicksort(left, key) + middle + quicksort(right, key)

def sort_by_height_difference(my_height, heights):
    # 定义计算身高差的关键字函数
    def height_difference(height):
        return abs(height - my_height)

    # 使用快速排序对身高列表进行排序
    sorted_heights = quicksort(heights, key=height_difference)
    return sorted_heights

# 示例输入
my_height = int(input("请输入小明的身高: "))
heights = list(map(int, input("请输入其他小朋友的身高列表（以空格分隔）: ").split()))

# 获取排序结果
sorted_heights = sort_by_height_difference(my_height, heights)

# 输出结果
print("排序后的身高列表:", sorted_heights)
