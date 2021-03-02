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

-   ...

2. FOR i = 1 to arr.length

3. int j <-- i - 1
4. int temp <-- arr[i]
5. WHILE j >= 0 AND temp < arr[j]
6. arr[j + 1] <-- arr[j]
7. j <-- j - 1
8. arr[j + 1] <-- temp

Now that we have walked through what each line does lets take an unsorted list and look at what every loop looks like to sort it.
