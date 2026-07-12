from typing import List;
def encode(strs: List[str]) -> str:
    def asciiConvert(s:str):
        result=""
        for char in s:
            order=ord(char)
            res=""
            if order<10:
                res=f"00{order}"
            elif order<100:
                res=f"0{order}"
            else:
                res=str(order)
            result+=(f"{res}") 
        return result
    encoded_string=""
    for s in strs:
        encoded_string+=asciiConvert(s)+"300"
    return encoded_string

def decode(s: str) -> List[str]:
    i=0
    decoded_strs=[]
    while i+2<len(s):
        deli=s[i:i+3]
        chars=""
        while deli!="300":
            chars+=chr(int(deli))
            i+=3
            deli=f"{s[i]}{s[i+1]}{s[i+2]}"
        
        decoded_strs.append(chars)
        i+=3

        
    return decoded_strs
