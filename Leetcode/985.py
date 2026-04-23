def sumEvenAfterQueries( nums, queries):
    evens=0
    output=[]
    for num in nums:
        if num%2==0:
            evens+=num
    for val,index in queries:
        if nums[index]%2==0:
            evens-=nums[index]
        nums[index]+=val
        if nums[index]%2==0:
            evens+=nums[index]
        output.append(evens)
    return output