from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # for _ in range(k):
        #     ele = nums[-1]
        #     for i in range(len(nums) - 1):
        #         nums[i + 1] = nums[i]
        #     nums[0] = ele
        # return nums
        # i = 0
        # while i < len(nums) - 1:
        #     nums[i], nums[i + 1] = nums[i + 1], nums[i]
        #     i += 1
        # return nums
        for _ in range(k):
            ele = nums[-1]
            i = len(nums) - 1
            while i >= 0:
                nums[i] = nums[i - 1]
                i -= 1
            nums[0] = ele
        return nums


sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 1))
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 2))
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 0))
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 9))
