def merge_sorted_array(nums1,nums2):
    a,b=len(nums1),len(nums2)
    sorted_list=[]
    i=j=0
    
    while i<a and j<b:
        if nums1[i]>nums2[j]:
            sorted_list.append(nums2[j])
            j+=1
        else:
            sorted_list.append(nums1[i])
            i+=1
            
    while i<a:
        sorted_list.append(nums1[i])
        i+=1
        
    while j<b:
        sorted_list.append(nums2[j])
        j+=1
        
    return sorted_list
