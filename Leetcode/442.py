def findDuplicates(self, nums) :
    #oh my go
    res=[]
    for num in nums:
        idx=abs(num)-1
        if nums[idx]<0:
            res.append(abs(num))
        else:
            nums[idx]=-nums[idx]
    return res