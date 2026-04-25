def get_next(number):
    summ=0
    while number>0:
        summ+=(number%10) ** 2
        number//=10
    return summ

def isHappy( n) :
    slow=n
    fast=get_next(n)
    while fast!=1 and fast!=slow:
        slow=get_next(slow)
        fast=get_next(get_next(fast))

    return fast==1
