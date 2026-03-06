def reverseWords(s: str) -> str:
    s.strip()
    arr=[]
    word=[]
    for i in range(len(s)):
        if not s[i].isspace():
            word.append(s[i])
        if s[i].isspace() and len(word)!=0:
            arr.append("".join(word))
            word=[]
    if word:
        arr.append("".join(word))
    arr.reverse()
    return " ".join(arr)