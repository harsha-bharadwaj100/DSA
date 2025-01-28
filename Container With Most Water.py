from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0  # max area
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


### Test cases

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution().maxArea(height))
