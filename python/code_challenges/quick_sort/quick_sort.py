def sort_quick(arr, left, right):
    if left < right:
        posiition = partition(arr, left, right)

        sort_quick(arr, left, posiition - 1)

        sort_quick(arr, posiition + 1, right)

    return arr


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1

    for i in range(len(arr)):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)

    return low + 1


def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
