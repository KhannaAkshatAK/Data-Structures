def bubble_sort(nums):
    n=len(nums)
    for i in range(n-1):
        swap=False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swap=True
        if swap == False:
            break
    return nums
