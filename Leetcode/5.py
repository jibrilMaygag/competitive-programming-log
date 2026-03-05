def longestPalindrome(self, s: str) -> str:
    longest=''
    for i in range(len(s)):
        l,r=i,i
        #check for odd substring palindromes by expanding until l and r don't match
        while l>=0 and r<len(s) and s[l]==s[r]:
            if len(longest)<r-l+1  :
                longest=s[l:r+1]
            l-=1
            r+=1
        #check for even ones
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if len(longest)<r-l+1  :
                longest=s[l:r+1]
            l-=1
            r+=1
    return longest
