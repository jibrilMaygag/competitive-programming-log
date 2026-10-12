def partitionLabels( s: str) -> list[int]:
    last={}
    result=[]
    start,end=0,0
    for i in range(len(s)):
        last[s[i]]=i
    
    for i in range(len(s)):
        char = s[i]
        if last[char]!=i:
            end=max(end,last[char])
        if end==i:
            result.append(end-start+1)
            start=end=i+1
    return result
print(partitionLabels("asdbdbsajj"))