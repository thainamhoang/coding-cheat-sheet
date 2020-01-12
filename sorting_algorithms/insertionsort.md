# Insertion Sort

Insertion sort is a simple sorting algorithm working by comparing the next item in an array with the before items, and then add that item to the corresponding position. 

## Time Complexity
| Best | Average| Worst |
| -----|:------:| -----:|
| O(N) | O(N^2) | O(N^2)|

## Auxiliary Space: O(1)

### Java
```java
public static void insertionSort(int[] sortingArray) {
    for (int i = 1; i < sortingArray.length; i++) {
        int currentMin = sortingArray[i];
        int j = i - 1;
        while (j >= 0 && sortingArray[j] > currentMin) {
            sortingArray[j + 1] = sortingArray[j];
            j -= 1;
        }
        sortingArray[j + 1] = currentMin;
    }
}
```

### Python
```python
def insertion_sort(sorting_array):
    length = len(sorting_array)
    keep_going = False
    for i in range (length):
        current_min = sorting_array[i]
        j = i - 1
        while j >= 0 and sorting_array[j] > current_min:
            sorting_array[j + 1] = sorting_array[j]
            j -= 1
        sorting_array[j + 1] = current_min
        keep_going = True
    
    if keep_going:
        return insertion_sort(sorting_array)
    else:
        return sorting_array
```

Using Python iterators
```python
def insertion_sort(sorting_array):
    keep_going = False
    for i, value in enumerate(sorting_array):
        for j in range(i - 1, -1, -1):
            if sorting_array[j] > value:
                sorting_array[j + 1] = sorting_array[j]
                sorting_array[j] = value
                keep_going = True
    if keep_going:
        return insertion_sort(sorting_array)
    else:
        return sorting_array
```