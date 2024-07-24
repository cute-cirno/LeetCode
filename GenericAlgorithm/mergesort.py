def merge_sort(arr, left, right):
    if left < right:
        # 找到中间的索引
        middle = (left + right) // 2
        
        # 递归地对左半部分和右半部分进行排序
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        
        # 合并两个已排序的部分
        merge(arr, left, middle, right)

def merge(arr, left, middle, right):
    # 创建临时数组存储左右两部分
    left_temp = arr[left:middle + 1]
    right_temp = arr[middle + 1:right + 1]
    
    # 初始化指针
    i = 0  # 左临时数组的起始索引
    j = 0  # 右临时数组的起始索引
    k = left  # 合并的数组的起始索引

    # 合并回arr中
    while i < len(left_temp) and j < len(right_temp):
        if left_temp[i] <= right_temp[j]:
            arr[k] = left_temp[i]
            i += 1
        else:
            arr[k] = right_temp[j]
            j += 1
        k += 1

    # 如果左侧或右侧还有剩余元素，直接复制回arr
    while i < len(left_temp):
        arr[k] = left_temp[i]
        i += 1
        k += 1

    while j < len(right_temp):
        arr[k] = right_temp[j]
        j += 1
        k += 1

# 使用归并排序的函数
array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array, 0, len(array) - 1)
print("Sorted Array:", array)
