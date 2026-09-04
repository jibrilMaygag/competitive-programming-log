def buddyStrings( s, goal):
    if len(s)!=len(goal):
        return False
    diff=[]
    for i in range(len(s)):
        if s[i]!=goal[i]:
            diff.append(i)
        if len(diff)>2:
            return False
    if len(diff)==0:
        duplicate= len(s)!=len(set(s))
        return duplicate
    if len(diff)!=2:
        return False
    i,j=diff
    return s[i]==goal[j] and s[j]==goal[i]