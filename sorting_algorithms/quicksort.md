# Quick Sort

Quick Sort is a [Divide and Conquer](/algorithms/divide_and_conquer.md) algorithm working by picking an element in the array as 'pivot' and partition the array around the pivot. There are many ways to pick a pivot, including:
* First element as pivot
* Last element as pivot
* Middle element as pivot
* Random element as pivot
These approachs will use first and random elements as pivot. 

## Time Complexity
| Best | Average| Worst |
| -----|:------:| -----:|
| O(N * log(N)) | O(N * log(N)) | O(N^2)|

## Auxiliary Space: O(log(N))

### Java
```java
public static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

public static void quickSort(int[] sortingArray, int begin, int end) {
    if (end <= begin) return;
    
    int pivot = begin;
    int less = begin;
    int more = end;
    
    while (pivot <= more) {
        if (sortingArray[pivot] < sortingArray[less]) {
            swap(sortingArray, pivot, less);
            
            pivot++;
            less++;
        }
        else if (sortingArray[less] < sortingArray[pivot]) {
            swap(sortingArray, pivot, more);
            
            more--;
        }
        else {
            pivot++;
        }
    }
    quickSort(sortingArray, begin, less - 1);
    quickSort(sortingArray, more + 1, end);
}
```

Random pivot
```java
import java.util.Random;

public static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

public static int partition(int[] sortingArray, int begin, int end) {
    int pivotValue = sortingArray[end];
    int pivotIndex = begin;

    for (int j = begin; j < end; j++) {
        if (sortingArray[j] <= pivotValue) {
            swap(sortingArray, pivotIndex, j);
            pivotIndex = pivotIndex + 1;
        }
    }
    swap(sortingArray, pivotIndex, end);
    return pivotIndex;
}
	
public static int randomPartition(int[] sortingArray, int begin, int end) {
    int randomPivot = (int)Math.floor(Math.random() * (end - begin + 1) + begin);
    swap(sortingArray, end, randomPivot);
    return partition(sortingArray, begin, end);
}

public static void randomQuickSort(int[] sortingArray, int begin, int end) {
    if (begin < end) {
        int pivot = randomPartition(sortingArray, begin, end);
        randomQuickSort(sortingArray, begin, pivot - 1);
        randomQuickSort(sortingArray, pivot + 1, end);
    }
}
```

### Python
```python
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(sorting_array, begin, end):
    if end <= begin: 
        return
    pivot = begin
    less = begin
    more = end

    while pivot <= more:
        if sorting_array[pivot] < sorting_array[less]:
            swap(sorting_array, pivot, less)
            pivot += 1
            less += 1
        elif sorting_array[less] < sorting_array[pivot]:
            swap(sorting_array, pivot, more)
            more -= 1
        else:
            pivot += 1
    
    quick_sort(sorting_array, begin, less - 1)
    quick_sort(sorting_array, more + 1, end)
    return sorting_array
``` 

Random pivot
```python
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(sorting_array, begin, end):
    pivot = begin
    i = begin - 1
    j = end + 1
    while True:
        while True:
            i += 1
            if sorting_array[i] >= sorting_array[pivot]:
                break
        while True:
            j -= 1
            if sorting_array[j] <= sorting_array[pivot]:
                break
        if i >= j:
            return j
        swap(sorting_array, i, j)

def partition_rand(sorting_array, begin, end):
    random_pivot = random.randrange(begin, end)
    swap(sorting_array, begin, random_pivot)
    return partition(sorting_array, begin, end)

def quick_sort(sorting_array, begin, end):
    if begin < end:
        pivot_index = partition_rand(sorting_array, begin, end)
        quick_sort(sorting_array, begin, pivot_index)
        quick_sort(sorting_array, pivot_index + 1, end)
```