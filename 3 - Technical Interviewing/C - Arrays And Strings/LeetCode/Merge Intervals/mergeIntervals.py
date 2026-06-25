from typing import List


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