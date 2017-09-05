def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newAttr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newAttr.append(arr.pop(smallest_index))
    return newAttr


print(selectionSort([5, 3, 6, 2, 10]))