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
                ^
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

### Second run through the for loop

before the while loop

```Python
i = 2
j = 1
temp = 23
sort_list = [4, 8, 23, 42, 16, 15]

```

So evaluating the values for the while loop j is greater than or equal to 0 but the temp value (23) **IS NOT** less than sort_list at j (8) so we do not enter the while loop.

```Python
i = 2
j = 1
temp = 23
sort_list = [4, 8, 23, 42, 16, 15]
                ^
```

J does decrement because we did not enter the while loop so 23 stays at its original index.

### Third run through the for loop

before the while loop

```Python
i = 3
j = 2
temp = 42
sort_list = [4, 8, 23, 42, 16, 15]
```

Once again evaluating the values for the while loop j is greater than or equal to 0 but the temp value (42) **IS NOT** less than sort_list (23) at j so we do not enter the while loop.

```Python
i = 2
j = 1
temp = 23
sort_list = [4, 8, 23, 42, 16, 15]
                        ^
```

J does decrement because we did not enter the while loop so 42 stays at its original index.

### Fourth run through the for loop

before the while loop

```Python
i = 4
j = 3
temp = 16
sort_list = [4, 8, 23, 42, 16, 15]
```

So evaluating the values for the while loop j is greater than or equal to 0 and the temp value (16) is less than sort_list at j (42). So we enter the while loop.

We then move 42 to index 4 because it is greater than 16. We also decrement j.

```Python
i = 4
j = 2
temp = 16
sort_list = [4, 8, 23, 42, 42, 15]
```

Since j is still greater than or equal to 0 AND 16 is less than 23 we go through the while loop again.

```Python
i = 4
j = 2
temp = 16
sort_list = [4, 8, 23, 42, 42, 15]
```

We then move 23 to index 3 because it is greater than 16. We decrement j again.

```Python
i = 4
j = 1
temp = 16
sort_list = [4, 8, 23, 23, 42, 15]
```

After we exit the while loop we then assign the temp value to index 2

```Python
i = 4
j = 1
temp = 16
sort_list = [4, 8, 16, 23, 42, 15]
```

### Last run through the for loop

before the while loop

```Python
i = 5
j = 4
temp = 15
sort_list = [4, 8, 16, 23, 42, 15]
```

So evaluating the values for the while loop j is greater than or equal to 0 and the temp value (15) is less than sort_list at j (42). So we enter the while loop.

We then move 42 to index 5 because it is greater than 15. We also decrement j.

```Python
i = 5
j = 3
temp = 15
sort_list = [4, 8, 16, 23, 42, 42]
```

Since j is still greater than or equal to 0 AND 15 is less than 23 we go through the while loop again.

We then move 23 to index 4 because it is greater than 15. We decrement j again.

```Python
i = 5
j = 2
temp = 15
sort_list = [4, 8, 16, 23, 23, 42]
```

Since j is STILL greater than or equal to 0 AND 15 is less than 16 we go through the while loop again.

We then move 16 to index 3 because it is greater than 15. We decrement j again.

```Python
i = 5
j = 1
temp = 15
sort_list = [4, 8, 16, 16, 23, 42]
```

We then exit the while loop because 15 IS NOT less than 8. So we then assign the temp value to index 2

```Python
i = 5
j = 1
temp = 15
sort_list = [4, 8, 15, 16, 23, 42]
```

NOW WE HAVE A SORTED LIST!
