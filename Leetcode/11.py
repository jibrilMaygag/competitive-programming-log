from collections import List
def maxArea(self, height: List[int]) -> int:
    i=0
    j=len(height)-1
    area=0
    while i<j:
        length=j-i
        width=min(height[i],height[j])
        area=max(length*width,area)
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return area