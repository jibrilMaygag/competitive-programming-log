from collections import Counter
def topKFrequent( nums, k):
    hashMap=Counter(nums)
    sortedArr=sorted(hashMap.items(),key=lambda x:x[1])
    return [el[0] for el in sortedArr[-k:]]
