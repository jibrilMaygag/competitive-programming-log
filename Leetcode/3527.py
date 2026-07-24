from collections import defaultdict,List
def findCommonResponse(responses: List[List[str]]) -> str:
    freq=defaultdict(int)
    for day in responses:
        sett=set(day)
        for response in sett:
            freq[response]+=1
    result=sorted(freq.keys(),key=lambda k : (-freq[k],k))
    return result[0] if result else ""
    