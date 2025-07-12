from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = i
            else:
                if abs(pos[nums[i]] - i) <= k:
                    return True
                else:
                    pos[nums[i]] = i
        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3))
print(sol.containsNearbyDuplicate([99, 99], 1))
