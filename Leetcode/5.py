
def longestPalindrome(s):
    largest=''
    
    for i in range(len(s)):
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            length=r-l+1
            if length>len(largest):
                largest=s[l:r+1]
            l-=1
            r+=1
    return largest
print(longestPalindrome("abadadads"))