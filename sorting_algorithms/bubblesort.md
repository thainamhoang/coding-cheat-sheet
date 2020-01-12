# Bubble Sort

Bubble Sort is the simplest sorting algorithm working by continuously swapping adjacent elements if they are in wrong order. 

## Time Complexity
| Best | Average| Worst |
| -----|:------:| -----:|
| O(N) | O(N^2) | O(N^2)|

## Auxiliary Space: O(1)

### Java 
```java
public static void bubbleSort(int[] sortingArray) {
    for (int i = 0; i < sortingArray.length - 1; i++) {
        for (int j = 0; j < sortingArray.length - i - 1; j++) {
            if (sortingArray[j] > sortingArray[j + 1]) {
                int temp = sortingArray[j];
                sortingArray[j] = sortingArray[j + 1];
                sortingArray[j + 1] = temp;
            }
        }
    }
}
```

### Python 
```python
def bubble_sort(sorting_array):
    length = len(sorting_array)
    keep_going = False
    for i in range (length - 1):
        for j in range (length - i - 1):
            if (sorting_array[j] > sorting_array[j + 1]):
                sorting_array[j], sorting_array[j + 1] = sorting_array[j + 1], sorting_array[j]
                keep_going = True
    if keep_going:
        return bubble_sort(sorting_array)
    else:
        return sorting_array
```