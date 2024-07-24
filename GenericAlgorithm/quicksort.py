def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)  # 递归排序枢轴左边的部分
        quicksort(arr, pivot_index + 1, high) # 递归排序枢轴右边的部分

def partition(arr, low, high):
    pivot = arr[high]  # 选择最后一个元素作为枢轴
    i = low        # 找到小于或等于枢轴的元素的位置
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# 使用快速排序的函数
def quick_sort(arr):
    quicksort(arr, 0, len(arr) - 1)

# 测试快速排序
array = [38, 27, 43, 3, 9, 82, 10]
quick_sort(array)
print("Sorted Array:", array)
