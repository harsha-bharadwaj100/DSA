from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        maxsum = -float("inf")

        for i in range(1, len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxsum = max(cursum, maxsum)

        return maxsum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
print(obj.maxSubArray(nums))
