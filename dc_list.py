def sum_list(arr):
    """use dc to sum arr"""
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_list(arr[1:])


# recursive handle 
arr = [1, 2, 3, 4]
print(sum_list(arr))


def cal_maximum_field(height, width):
    res = height - width
    if res == width:
        return width
    else:
        minimum = min(height, width)
        maximum = max(height, width)
        res_max = max(maximum - minimum, minimum)
        res_min = min(maximum - minimum, minimum)
        return cal_maximum_field(res_max, res_min)


print(cal_maximum_field(1680, 640))


def cal_list_num(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + cal_list_num(arr[1:])


arr = [1, 2, 3, 4, 5]
print(cal_list_num(arr))


# 哈哈哈
def find_max_num(arr, maximum):
    if len(arr) == 0:
        return maximum
    else:
        now = arr.pop()
        minimum = now

        if now > maximum:
            minimum = maximum
            maximum = now

        while minimum in arr:
            arr.remove(minimum)

        return find_max_num(arr, maximum)    


arr = [1, 2, 3, 4, 9, 3, 2, 10, 34, 34]
print(find_max_num(arr, arr[0]))
        

def binary_search(arr, l, r, target):
    if l >= r:
        return None

    mid = int((l + r) / 2)

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, r, target)
    else:
        return binary_search(arr, l, mid - 1, target)


arr = [1, 3, 5, 7, 9]
result = binary_search(arr, 0, len(arr), 9)
if result is not None:
    print("The target index is " + str(result))
else:
    print("I'm sorry, we can't find it!")