from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = []
        tempval = intervals[0][:]
        i = 0
        while i < len(intervals) - 1:
            if tempval[1] >= intervals[i + 1][0]:
                tempval[1] = max(tempval[1], intervals[i + 1][1])
                i += 1
            else:
                result.append(tempval)
                tempval = intervals[i + 1]
                i += 1

        result.append(tempval)
        return result


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [3, 4], [8, 15], [15, 18]]))
