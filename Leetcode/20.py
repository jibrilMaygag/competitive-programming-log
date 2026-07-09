
def isValid( s) :
    h={'}':'{',']':'[',')':'('}
    stack=[]
    for el in s:
        if el not in h:
            stack.append(el)
        else:
            if stack and stack[-1]==h[el]:
                stack.pop()
            else:
                return False
    return not stack




