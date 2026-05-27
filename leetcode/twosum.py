def twoSum(nums, target):
    hashmap = {}  # stores number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
# Example usage:
nums = [2, 7, 11, 15]   