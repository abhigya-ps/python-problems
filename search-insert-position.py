def searchInsert(nums, target):
    # binary search
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return l    
    # linear search
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    #     if nums[i] > target:
    #         return i
    # return len(nums)

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))


nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 0
print(searchInsert(nums, target))