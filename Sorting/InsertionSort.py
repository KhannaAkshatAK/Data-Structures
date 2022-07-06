def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        j=i-1
        while j>=0 and nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            j-=1
    return nums
