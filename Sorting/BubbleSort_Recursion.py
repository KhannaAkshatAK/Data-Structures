def bubble_sort(nums):
    n=len(nums)
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            nums=bubble_sort(nums)
    return nums
