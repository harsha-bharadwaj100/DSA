from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        right = k - 1
        res = []
        while right < len(nums):
            queue = nums[left : right + 1]
            res.append(max(queue))
            left += 1
            right += 1
        return res


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
