def insertion_sort(nums,n):
    if n>=1:
        return nums
    nums=insertion_sort(nums,n-1)
    i=n-2
    while (i>=0 and nums[i]>nums[i+1]):
        nums[i],nums[i+1]=nums[i+1],nums[i]
        i-=1
    return nums
