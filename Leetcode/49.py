def sortC(s):
    arr=[0]*26
    for char in s:
        arr[ord(char)-ord('a')]+=1

    return "".join([f"{chr(i+ord('a'))}{arr[i]}" for i in range(len(arr)) if arr[i]!=0])

def groupAnagrams( strs):
    res={}
    for str in strs:
        sorted=sortC(str) #"10001000000000000001000000" str="ate"
        if sorted in res:
            res[sorted].append(str)
        else:
            res[sorted]=[str]
    return [value for _,value in res.items()]

