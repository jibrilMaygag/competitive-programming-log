
def largestPerimeter( nums: list[int]) -> int:
    nums.sort(reverse=True)
    a,b=0,1
    for i in range(2,len(nums)):
        c=i
        if nums[b]+nums[c]>nums[a]:
            return nums[a]+nums[b]+nums[c]
        a=b
        b=c

    return 0
print(largestPerimeter([2,3,2,1,5,4,8]))