from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.psum = 0
        self.prefix_sum = [0]
        for ele in self.nums:
            self.psum += ele
            self.prefix_sum.append(self.psum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray([-2, 0, 3, -5, 2, -1])
# left, right = [0, 2]
obj = NumArray([5, 2, 3, 4, 7])
left, right = [0, 4]
param_1 = obj.sumRange(left, right)
print(param_1)
