# Merge Sort

Merge Sort is a [Divide and Conquer](/algorithms/divide_and_conquer) algorithm. It first divides the array into two halves, call itselfs for the two halves, sorts and then merges. 

## Time Complexity
| Best | Average| Worst |
| -----|:------:| -----:|
| O(N * log(N)) | O(N * log(N)) | O(N * log(N))|

## Auxiliary Space: O(N)

### Java
```java
public static void mergeSort(int[] sortingArray, int arrayLength) {
    if (arrayLength == 1) return;
    int middlePoint = arrayLength / 2;
    int[] leftArray= new int[middlePoint];
    int[] rightArray = new int[arrayLength - middlePoint];
    
    for (int i = 0; i < middlePoint; i++) {
        leftArray[i] = sortingArray[i];
    }
    for (int j = middlePoint; j < arrayLength; j++) {
        rightArray[j - middlePoint] = sortingArray[j];
    }
    mergeSort(leftArray, middlePoint);
    mergeSort(rightArray, arrayLength - middlePoint);
    
    merge(sortingArray, leftArray, rightArray, middlePoint, arrayLength - middlePoint);
}
	
public static void merge(int[] sortingArray, int[] leftArray, int[] rightArray, int left, int right) {
    int i = 0, j = 0, k = 0;
    while (i < left && j < right) {
        if (leftArray[i] <= rightArray[j]) {
            sortingArray[k++] = leftArray[i++];
        }
        else {
            sortingArray[k++] = rightArray[j++];
        }
    }
    while (i < left) {
        sortingArray[k++] = leftArray[i++];
    }
    while (j < right) {
        sortingArray[k++] = rightArray[j++];
    }  
}
```

Using ArrayList
```java
public static void merge(ArrayList<Integer> sortingArray) {
    if (sortingArray.size() == 1) return;
    
    int middlePoint = sortingArray.size() / 2;
    ArrayList<Integer> leftArray = new ArrayList<Integer>();
    ArrayList<Integer> rightArray = new ArrayList<Integer>();
    
    for (int i = 0; i < middlePoint; i++) leftArray.add(sortingArray.remove(0));
    while (sortingArray.size() != 0) rightArray.add(sortingArray.remove(0));
    
    merge(leftArray);
    merge(rightArray);
    
    while (leftArray.size() != 0 && rightArray.size() != 0) {
        if (leftArray.get(0).compareTo(rightArray.get(0)) < 0) {
            sortingArray.add(leftArray.remove(0));
        }
        else {
            sortingArray.add(rightArray.remove(0));
        }
    }
    
    while (leftArray.size() != 0 ) {
        sortingArray.add(leftArray.remove(0));
    }
    while (rightArray.size() != 0 ) {
        sortingArray.add(rightArray.remove(0));
    }
}
```

### Python
```python
def merge_sort(sorting_array):
    if len(sorting_array) == 1: 
        return sorting_array
    middle = len(sorting_array) / 2
    left = sorting_array[:middle]
    right = sorting_array[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    array = []
    while left or right:
		if left and right:
			if left[0] < right[0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		elif left:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	return result
```