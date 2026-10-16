def minPatches(nums: list[int], n: int) -> int:
    i=0
    result=0
    l=0
    while (l<n):
        if i>=len(nums) or nums[i]>l+1:
            l+=l+1
            result+=1
            continue
        else:
            l+=nums[i]
            i+=1
    return result


print(minPatches([1,3],6))

