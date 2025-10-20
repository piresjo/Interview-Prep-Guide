# Jumping On Clouds

## Things To Note

In the input character array:

- '0' -> Safe
- '1' -> Unsafe

The beginning and end of the array are always safe.

Can jump one or two characters ahead.

## Solution (Java)

```java
static int jumpingOnClouds(int[] c) {
  int minPath = 0;
  int i = 0;

  while (i < c.length() - 1) {
    if (i == c.length() - 2) {
      i++;
      minPath++;
    } else {
      if (c[i+2] == 0) {
        i += 2;
        minPath++;
      } else {
        i++;
        minPath++;
      }
    }
  }
  return minPath++;
}
```
