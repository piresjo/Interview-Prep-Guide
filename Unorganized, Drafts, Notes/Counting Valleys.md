# Counting Valleys

## Things To Note

Here, we're referring to `valleys` as consecutive characters below sea level and `mountains` as consecutive characters over sea level.

## Solution (Java)

```java
static int countingValleys(int n, String s) {
  int level = 0;
  int valleys = 0;

  for (char c: s.toCharArray()) {
    if (c == 'u') {
      level++;
    } else {
      level--;
    }
    if (level == 0 && c == 'u') {
      valleys++;
    }
  }
  return valleys;
}
```
