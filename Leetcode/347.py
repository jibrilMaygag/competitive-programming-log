from collections import Counter
def topKFrequent( nums, k) :
    hashMap=Counter(nums)
    arr=[[] for _ in range(len(nums)+1)]
    for value,freq in hashMap.items():
        arr[freq].append(value)
    result=[]
    for i in range(len(arr)-1,-1,-1):
        for v in arr[i]:
            result.append(v)
            if len(result)==k:
                return result
    return []