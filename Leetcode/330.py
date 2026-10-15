def minPatches(nums: list[int], n: int) -> int:
    i=0
    result=0
    l=0
    while (l<n):
        if nums[i]>l+1:
            nums.insert(i,l+1)
            result+=1
            continue
        if nums[i]==1:
            l=max(l,1)
            i+=1
            continue
        l=max(l,nums[i]+l)
        i+=1

    return result
print(minPatches([1,3],6))

