def merge(intervals):
    if not intervals or len(intervals) <= 1:
        return intervals
        
    returnList = []
    intervals.sort(key=lambda x: x[0])
    currInterval = intervals[0]
    returnList.append(currInterval)
        
    for interval in intervals:
        currBegin = currInterval[0]
        currEnd = currInterval[1]
        nextBegin = interval[0]
        nextEnd = interval[1]
            
        if currEnd >= nextBegin:
            currInterval[1] = max(currEnd, nextEnd)
        else:
            currInterval = interval
            returnList.append(currInterval)
    return returnList