def beautySum(self, s: str) -> int:
    def getMax(arr):
        maxx=0
        for i in range(26):
            maxx=max(maxx,arr[i])
        return maxx
    def getMin(arr):
        minn=float("inf")
        for i in range(26):
            if arr[i]!=0:
                minn=min(minn,arr[i])
        return minn
    summ=0
    for i in range(len(s)):
        arr=[0]*26
        for j in range(i,len(s)):
            arr[ord(s[j])-ord('a')]+=1
            beauty=getMax(arr)-getMin(arr)
            summ+=beauty
    
    return summ