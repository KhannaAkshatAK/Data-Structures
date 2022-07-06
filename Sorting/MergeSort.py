def merge_sort(nums):
    n=len(nums)
    if n<=1:
        return nums
    
    mid=n//2
    
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge_sorted_array(left,right)
