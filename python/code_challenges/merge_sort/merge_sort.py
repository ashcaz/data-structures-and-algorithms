
def sort_merge(list_to_sort:list) -> list:
    n = len(list_to_sort)

    if n > 1:
        mid = n/2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        sort_merge(left)

        sort_merge(right)

        merge(left, right, list_to_sort)

    
    def merge(left, right, list_to_sort):
        i,j,k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list_to_sort[k] = left[i]
                i += 1

            else:
                list_to_sort[k] = right[j]
                j += 1

            k +=1

        if i = len(left):
            while i < len(left):
                list_to_sort[k] = left[i]
                i += 1
                k += 1
        else:
            while j < len(right):
                list_to_sort[k] = right[j]
                j += 1
                k += 1