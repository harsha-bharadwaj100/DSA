from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        print(nums)
        while i < len(nums) and i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
            print(nums)
        return i


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
