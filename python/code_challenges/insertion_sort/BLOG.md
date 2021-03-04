# Insertion Sort

## Pseudocode

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

So lets walk through this line by line.

1. InsertionSort(int[] arr)

    - In this step we are defining a function that takes in a list of integers

2. FOR i = 1 to arr.length

    - the line starts a for loop. It will loop though the array starting at index 1 and go the full length of the array

3. int j <-- i - 1

    - this line creates variable named j that is assigned the value of i-1

4. int temp <-- arr[i]

    - create a temp variable that is assigned the value of the array at index i

5. WHILE j >= 0 AND temp < arr[j]

    - next it is creating a while loop that will continue to run untill variable j is greater than or equal to 0 AND the temp variable is less than the array at index j.

6. arr[j + 1] <-- arr[j]

    - since the temp variable is < array at index j we need to move it 1 index to the right in order for the array to properly sort

7. j <-- j - 1

    - this line decrements variable j

8. arr[j + 1] <-- temp

    - this statement assigns the temp variable at array at index j+1

This will continue until we have gone the whole way through the array

## Walk through

Now that we have walked through what each line does lets take an unsorted list and look at what every loop looks like to sort it.

```Python
list_to_sort = [8,4,23,42,16,15]
```

CODE:

```Python
def sort_func(sort_list: list) -> list:

    for i in range(1, len(sort_list)):
        j = i - 1
        temp = sort_list[i]

        while j >= 0 and temp < sort_list[j]:

            sort_list[j + 1] = sort_list[j]
            j = j - 1

        sort_list[j + 1] = temp

    return sort_list
```

### First run through the for loop

before the while loop

```Python
i = 1
j = 0
temp = 4
sort_list = [8, 4, 23, 42, 16, 15]
```

So evaluating the values for the while loop j is greater than or equal to 0 and the temp value (4) is less than sort_list at j (8). So we enter the while loop.

We then move 8 to index 1 because it is greater than 4. We also decrement j so that we exit the while loop.

```Python
i = 1
j = -1
temp = 4
sort_list = [8, 8, 23, 42, 16, 15]
```

After we exit the while loop we then assign the temp value to index 1

```Python
i = 1
j = -1
temp = 4
sort_list = [4, 8, 23, 42, 16, 15]
```
