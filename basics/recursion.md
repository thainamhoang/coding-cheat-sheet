# Recursion
Recursion is a method which can call itself. [Here](https://www.youtube.com/watch?v=B0NtAFf4bvU) is a great explanation of how recursion works.

## Factorial
Factorial is a great basic example of how to use recursion

### Java
```java
public static long factorial (long n) {
    if (n <=1 ) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

### Python
```python
def factorial(n):
    if n <= 1:
        return 1;
    return n * factorial(n - 1)
```

## Memoization
Memoization is often used in recursion, especially with expensive values. The results of a method are stored so that they can be used later when called. 

### Java
```java
private static long[] fibonacciArray = new long[26];
public static long factorialMemo(long n) {
    long fibVal = 1;
    if (n <= 1) {
        return 1;
    }
    else if (fibonacciArray[(int) n]  != 0) {
        return fibonacciArray[(int) n];
    }
    else {
        fibVal = factorialMemo(n - 1);
        fibonacciArray[(int) n] = fibVal;
        return fibVal;
    }
}
```

### Python
```python
factorial_memo_array = {}

def factorial_memo(n):
    if n <= 1:
        return 1
    elif n not in factorial_memo_array:
        factorial_memo_array[n] = n * factorial(n - 1)
    return factorial_memo_array[n]
```

## Tail Recursion
Tail recursion is a recursion in which recursive call is the last thing executted by the method. Some programming languages, usually functional ones, optimize tail calls so they take up less room on the call stack. 

### Java
```java
public static long factorialTailRecur (long n, long a) {
    if (n == 0) {
        return a;
    }
    return factorialTailRecur(n - 1, n * a);
}

public static long factorial(long n) {
    return factorialTailRecur(n, 1);
}
```

### Python
```python
def factorial_tail_recur(n, running_total = 1):
    if n <= 1:
        return running_total
    return factorial(n - 1, n * running_total)
```