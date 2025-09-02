from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        size = len(nums)
        p = 0
        temp = nums[p]
        start_index = p
        for _ in range(size):
            nums[(p + k) % size], temp = temp, nums[(p + k) % size]
            p = (p + k) % size
            if p == start_index:
                p = (p + 1) % size
                start_index = p
        return nums


sol = Solution()
# print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 1))
# print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 2))
# print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 0))
# print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 9))
# print(sol.rotate([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(sol.rotate([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(sol.rotate([1, 2, 3, 4, 5, 6, 7, 8], 4))
print(sol.rotate([1, 2, 3, 4, 5, 6, 7, 8], 6))
