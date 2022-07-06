def partition(nums):
    pivot_index=0
    pivot=nums[0]
    
    start=1
    end=len(nums)-1
    
    while start<end:
        while nums[start]<=pivot:
            start+=1
        while nums[end]>=pivot:
            end-=1 
        if start<end:
            nums[start],nums[end]=nums[end],nums[start]
    nums[pivot_index],nums[end]=nums[end],nums[pivot_index]
