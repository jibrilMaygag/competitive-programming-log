def swap_case(s):
    result=[]
    for i in range(len(s)):
        if 97<=ord(s[i])<=122:
            result.append(s[i].upper())
        elif 65<=ord(s[i])<=97:
            result.append(s[i].lower())
        else:
            result.append(s[i])

    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)