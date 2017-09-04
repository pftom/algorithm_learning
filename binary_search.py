def binary_search(list, item):
    """search the target item in list"""
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))