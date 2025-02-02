from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_max = current_min = overall_max = nums[0]
        for num in nums[1:]:
            temp_max = max(num, current_max * num, current_min * num)
            current_min = min(num, current_max * num, current_min * num)
            current_max = temp_max
            overall_max = max(overall_max, current_max)
        return overall_max


nums = [-8, 2, 3, -2, -1, 4]
obj = Solution()
print(obj.maxProduct(nums))
