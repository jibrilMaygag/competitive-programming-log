import random


class RandomizedSet:

    def __init__(self):
        self.hash={}
        self.vals=[]

    def insert(self, val):
        check=val not in self.hash
        if check:
            self.vals.append(val)
            self.hash[val]=len(self.vals)-1
        return check
        

    def remove(self, val):
        check=val in self.hash
        if check:
            index=self.hash[val]
            self.vals[index]=self.vals[len(self.vals)-1]
            self.hash[self.vals[index]]=index
            self.vals.pop()
                
            del self.hash[val]
        return check
    def getRandom(self):
        ran=random.randint(0,len(self.vals)-1)
        return self.vals[ran]
        

