from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [int(x) for x in input("Input: nums = ").split()]
target = int(input("target: "))

output = twoSum(nums, target)
print("Output:", output)