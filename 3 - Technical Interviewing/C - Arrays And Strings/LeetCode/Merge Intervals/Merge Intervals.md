# Merge Intervals

## Problem

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

## Things To Note

The interval list is unsorted in any way.


## Solution Explained

Based off the problem, if we can sort the interval lists by the first element of the interval, we can then run through the list of intervals once.

That will be the first thing we do.

Once we have that, since we're returning a new list, we can set that up and define the first potential interval to go in there (which would be `intervals[0]`). Then we go through the sorted intervals. If the first element of the second interval is less than or equal to the end element of the first interval, we can merge the intervals. If the end element of the second interval is greater than the end element of the first interval, we can update the end element of the interval we'll be appending to the return list.

If not, then we push the merged interval to the return list and restart the process.

## Solution

```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
        
    returnList = []
    appendList = sortedIntervals[0]

    for i in range(len(sortedIntervals)):
        intervalVal = sortedIntervals[i]

        if intervalVal[0] <= appendList[1]:
            if intervalVal[1] > appendList[1]: 
                appendList[1] = intervalVal[1]
        else:
            returnList.append(appendList)
            appendList = intervalVal
    returnList.append(appendList)

    return returnList
```

## Analysis

In terms of time complexity, most in-language sorting algorithms are liniarithmic. The sorting is the most complex part of the solution time wise, so the overall time complexity is linearithmic.

In terms of space complexity, assuming the sorting algorithm used is constant, in the worst case, we need to create two new arrays of size `n` (the size of `intervals`). This yields us a linear space complexity.