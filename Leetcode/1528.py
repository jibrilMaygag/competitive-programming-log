def restoreString( s,indices):
    i=0
    s=list(s)
    while i<len(s):
        if i!=indices[i]:
            index=indices[i] 
            s[i],s[index]=s[index],s[i]
            indices[index],indices[i]=indices[i],indices[index]
        else:
            i+=1
        
    return "".join(s)
    