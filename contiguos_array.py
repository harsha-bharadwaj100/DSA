from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_difference = 0
        prefix_sums = {0: -1}
        csum = 0
        for i in range(len(nums)):
            csum += 1 if nums[i] == 0 else -1
            if csum in prefix_sums:
                difference = i - prefix_sums[csum]
                max_difference = max(difference, max_difference)
            else:
                prefix_sums[csum] = i
        return max_difference


sol = Solution()
print(sol.findMaxLength([0, 1, 0, 1, 0, 0, 1, 0, 0, 0]))
