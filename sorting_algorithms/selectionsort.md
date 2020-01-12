# Selection sort

Selection sort is a simple sorting algorithm by continuously finding the minimum element from unsorted part to put it at the beginning. The given array then separates into two parts: sorted and unsorted.

## Time Complexity
| Best   | Average| Worst |
| -------|:------:| -----:|
| O(N^2) | O(N^2) | O(N^2)|

## Auxiliary Space: O(1)

### Java
```java
public static void selectionSort(int[] sortingArray) {
    for (int i = 0; i < sortingArray.length; i++) {
        int minIndex = i;
        for (int j = i + 1; j < sortingArray.length; j++) {
            if (sortingArray[j] < sortingArray[minIndex]) {
                int temp = sortingArray[j];
                sortingArray[j] = sortingArray[minIndex];
                sortingArray[minIndex] = temp;
            }
        }
    }
}
```

### Python
```python
def selection_sort(sorting_array):
    length = len(sorting_array)
    keep_going = False
    for i in range (length):
        min_index = i
        for j in range (i + 1, length):
            if (sorting_array[j] < sorting_array[min_index]):
                sorting_array[j], sorting_array[min_index] = sorting_array[min_index], sorting_array[j]
                keep_going = True

    if keep_going:
        return selection_sort(sorting_array)
    else:
        return sorting_array
```