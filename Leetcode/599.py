from typing import List

def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    minn=float("inf")
    result=[]
    hashMap={list2[index]:index for index in range(len(list2))}
    for i,string in enumerate(list1):
        if string in hashMap:
            total=hashMap[string]+i
            if total <minn:
                minn=total
                result=[string]
            elif total == minn:
                result.append(string)
    return result