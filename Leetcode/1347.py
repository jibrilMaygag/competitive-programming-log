def minSteps( s: str, t: str) -> int:
    bucket=[0]*26
    for char in t:
        bucket[ord(char)-ord('a')]+=1
    for char in s:
        if bucket[ord(char)-ord('a')]>0:
            bucket[ord(char)-ord('a')]-=1

    return sum(bucket)

