def twoSum(nums: list[int], target: int) -> list[int]:
    hmap = set()
    for i in range(len(nums)):
        if target - nums[i] in hmap:
            return nums.index(target - nums[i]), i
        else:
            hmap.add(nums[i])


print(twoSum([2, 7, 11, 15], 9))
