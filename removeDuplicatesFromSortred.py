from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1

        return i + 1


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(sol.removeDuplicates([1, 1, 2]))
print(sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
