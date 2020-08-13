def twoSum(nums, target):

    if len(nums) <= 1:
        return False

    pairs = {}
    for i in range(len(nums)):
        if nums[i] in pairs:
            return [pairs[nums[i]], i]
        else:
            pairs[target - nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))