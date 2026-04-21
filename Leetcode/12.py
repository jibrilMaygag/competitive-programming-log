
def intToRoman(num) :
    symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    value=[   1000,900,500,400,100, 90,  50, 40,  10,  9,  5,   4,  1]
    result=[]
    for i  in range( len(symbols)):
        v=num//value[i]
        if v>0:
            result.append(symbols[i]*v)
            num%=value[i]
    return "".join(result)