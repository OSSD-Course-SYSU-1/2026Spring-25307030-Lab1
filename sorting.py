# sorting.py
def bubble_sort(arr):
    """
    冒泡排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已有序，无需再比较
        for j in range(0, n-i-1):
            # 交换元素，使较大元素后移
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", test_list)
    sorted_list = bubble_sort(test_list)
    print("排序后:", sorted_list)