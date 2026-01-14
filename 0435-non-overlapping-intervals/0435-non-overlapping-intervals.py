class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], x[0]))

        remove = 0
        prev = intervals[0]
        for i in intervals[1:]:
            if i[0] < prev[1]:
                remove += 1
            else:
                prev = i
        
        return remove