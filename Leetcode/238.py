from collections import List;
def productExceptSelf(self, nums: List[int]) -> List[int]:
    result=[]
    suffix=1
    for num in nums:
        suffix*=num
        result.append(suffix)
    suffix=1
    for i in range(len(nums)-1,-1,-1):
        left=1
        right=1
        if i>0:
            left=result[i-1]
        if i<len(nums)-1:
            right=suffix
        result[i]=left*right
        suffix*=nums[i]
    return result
