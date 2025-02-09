from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cursum = 0
        minlen = float("inf")

        while right < len(nums):
            cursum += nums[right]
            while cursum >= target:
                minlen = min(right - left + 1, minlen)
                cursum -= nums[left]
                left += 1

            right += 1

        return minlen


sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
