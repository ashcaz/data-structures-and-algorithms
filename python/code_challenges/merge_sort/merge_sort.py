def sort_merge(list_to_sort: list) -> list:
    def merge(left, right, list_to_sort):
        i, j, k = 0, 0, 0
        print(
            f"""
            left = {left}
            right = {right}
            i = {i}
            j = {j}
            k = {k}
        """
        )

        while i < len(left) and j < len(right):
            print(
                f"""
            inside while loop {k}
            left = {left}
            right = {right}
            i = {i}
            j = {j}
            k = {k}
        """
            )
            if left[i] <= right[j]:
                list_to_sort[k] = left[i]
                i += 1

                print(
                    f"""
                inside if 1
                left = {left}
                right = {right}
                i = {i}
                j = {j}
                k = {k}
            """
                )

            else:
                list_to_sort[k] = right[j]
                j += 1

                print(
                    f"""
                inside else1
                left = {left}
                right = {right}
                i = {i}
                j = {j}
                k = {k}
            """
                )

            k += 1

        if i == len(left):
            while j < len(right):
                list_to_sort[k] = right[j]
                j += 1
                k += 1

                print(
                    f"""
                inside if left
                left = {left}
                right = {right}
                i = {i}
                j = {j}
                k = {k}
            """
                )
        else:
            while i < len(left):
                list_to_sort[k] = left[i]
                i += 1
                k += 1

                print(
                    f"""
                inside else {k}
                left = {left}
                right = {right}
                i = {i}
                j = {j}
                k = {k}
            """
                )
        print("list: ", list_to_sort)
        return list_to_sort

    n = len(list_to_sort)

    if n > 1:
        mid = n // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        sort_merge(left)

        sort_merge(right)

        return merge(left, right, list_to_sort)

    else:
        return list_to_sort
