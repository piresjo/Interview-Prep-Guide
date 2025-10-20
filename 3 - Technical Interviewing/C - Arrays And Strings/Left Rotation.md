# Left Rotation

## Solution (Java)

```java
static int[] rotateLeft(int[] a, int d) {
  int[] returnTable = new int[a.length];
  int tempLoc;
  for (int i = 0; i < a.length; i++) {
    tempLoc = i - d;
    if (tempLoc < 0) {
      tempLoc += (a.length - 1);
    }
    returnTable[tempLoc] = a[i];
  }
  return returnTable;
}
```
