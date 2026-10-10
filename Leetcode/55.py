
def canJump( nums: list[int]) -> bool:
    n=len(nums)
    goal=n-1
    for i in range(n-2,-1,-1):
        if nums[i]>=(goal-i):
            goal=i
    return goal==0
print(canJump([5,1,2,0,0,1]))