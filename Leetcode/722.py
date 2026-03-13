from typing import List

def removeComments(source: List[str]) -> List[str]: 
    ans=[]
    inBlock=False
    lineBuffer=[]
    for line in source:
        i=0
        #new pure line
        if not inBlock:
            lineBuffer=[]
        while i<len(line):
            #start of block comment
            if not inBlock and line[i:i+2]=='/*':
                inBlock=True
                i+=2
            elif inBlock and line[i:i+2]=='*/':
                inBlock=False
                i+=2
            elif not inBlock and line[i:i+2]=='//':
                break

            elif not inBlock:
                lineBuffer.append(line[i])
                i+=1
            else:
                i+=1
        if not inBlock and lineBuffer:
            ans.append("".join(lineBuffer))
    return ans


