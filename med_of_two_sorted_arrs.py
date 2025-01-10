from typing import List
import statistics


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        m = len(nums1)
        n = len(nums2)
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                res.append(nums2[j])
                j += 1
            elif nums1[i] == nums2[j]:
                res.append(nums1[i])
                res.append(nums2[j])
                i += 1
                j += 1
        if i == m:
            while j < n:
                res.append(nums2[j])
                j += 1
        if j == n:
            while i < m:
                res.append(nums1[i])
                i += 1
        return statistics.median(res)


sol = Solution()
print(sol.findMedianSortedArrays([], [5, 6, 6, 8, 10, 12, 13]))
