def separateDigits( nums) :
    result=[]
    for num in nums:
        for digit in str(num):
            result.append(int(digit))
    return result

    