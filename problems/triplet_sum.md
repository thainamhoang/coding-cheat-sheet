# Triplet Sum
Give an array of elements. Find triplets in array whose sum is a number

#### Java
```java
public static void tripletSum(int[] arr, int arrLength, int sum) {
    boolean isFound = false;
    for (int i = 0; i < arrLength - 2; i++) {
        for (int j = i + 1; j < arrLength -  1; j++) {
            for (int k = j + 1; k < arrLength; k++) {
                if (arr[i] + arr[j] + arr[k] == sum) {
                    isFound = true;
                }
                else {
                    isFound = false;
                }
            }
        }
    }
}
```

#### Python
```python
    def tripletSum(arr, arrLength, sum):
        isFound = False
        for i in range (0, arrLength - 2):
            for j in range (i + 1, arrLength - 1):
                for k in range (j + 1, arrLength):
                    if (arr[i] + arr[j] + arr[k] == sum):
                        isFound = True
                    else:
                        isFound = False
```