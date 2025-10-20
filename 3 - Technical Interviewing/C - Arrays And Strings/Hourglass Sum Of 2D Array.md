# Hourglass Sum Of 2D Array

## Solution (Java)

```java
static int hourglassSum(int[][] arr) {
  int sum = Integer.min_value;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      int tempSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
      sum = (tempSum > sum) ? tempSum : sum;
    }
  }
  return sum;
}
```
