def longestPalindrome(self, s: str) -> str:
    def checkP(s):
        j=[]
        for k in range(len(s)-1,-1,-1):
            j.append(s[k])
        return s=="".join(j)
    largest=''
    for i in range(len(s)):
        for j in range(i,len(s)):
            if checkP(s[i:j+1]):
                if len(largest)<j-i+1:
                    largest=s[i:j+1]
    return s[0] if len(s)==1 else largest