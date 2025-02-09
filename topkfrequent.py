from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        min_heap = []
        print(freq)
        for num in freq:
            heapq.heappush(min_heap, (freq[num], num))
            print(min_heap)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            print(min_heap)
        print(min_heap)
        return [num for _, num in min_heap]


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4], 3))
# print(sol.topKFrequent([1], 1))
# print(sol.topKFrequent([1, 2], 2))
