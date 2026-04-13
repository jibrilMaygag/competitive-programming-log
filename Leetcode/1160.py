from typing import List

def countCharacters( words: List[str], chars: str) -> int:
    result=0
    base=[0]*26
    for char in chars:
        base[ord(char)-ord('a')]+=1
    for word in words:
        chars_arr=base[:]
        valid=True
        for char in word:
            idx=ord(char)-ord('a')
            if chars_arr[idx]<=0:
                valid=False
                break
            chars_arr[idx]-=1
        if valid:
            result+=len(word)
    return result