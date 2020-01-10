# Generate Binary Strings
Given a string contains '0', '1', and '?' (a wildcard character). Generate all binary strings that can be formed by replacing '?' as '0' or '1'.

### Java
```java
public static void replacing (char[] charArr, int i) {
		if (i == charArr.length) {
			System.out.println(charArr);
			return;
		}
		
		if (charArr[i] == '?') {
			for (char ch = '0'; ch <= '1'; ch++) {
				// Replace '?' with '0' and '1'
				charArr[i] = ch;
				
				// Recur for the remaining pattern
				replacing(charArr, i + 1);
				
				// Backtrack
				charArr[i] = '?';
			}
			return;
		}
		replacing(charArr, i + 1);
	}
```

### Python
```python
def replacing (string):
    if "?" not in string:
        print(string)
    else:
        replacing(string.replace("?", "0", 1))
        replacing(string.replace("?", "1", 1))
```