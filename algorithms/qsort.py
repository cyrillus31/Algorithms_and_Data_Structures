def qsort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    pivot = nums[len(nums)//2]
    return qsort([num for num in nums if num < pivot]) + [pivot] + qsort([num for num in nums if num > pivot])

print(qsort([12,433,5434,5,3,4,53,2345,8]))
