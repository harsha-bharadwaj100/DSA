from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        visited = set()
        max_len = 0

        for num in nums:
            if num not in visited:
                visited.add(num)
                count = 1

                # Expand to the left
                left = num - 1
                while left in numset and left not in visited:
                    visited.add(left)
                    count += 1
                    left -= 1

                # Expand to the right
                right = num + 1
                while right in numset and right not in visited:
                    visited.add(right)
                    count += 1
                    right += 1

                max_len = max(max_len, count)

        return max_len


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sol.longestConsecutive([1, 0, 1, 2]))
print(sol.longestConsecutive([0]))
print(sol.longestConsecutive([0, 0]))
print(sol.longestConsecutive([]))
print(sol.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
