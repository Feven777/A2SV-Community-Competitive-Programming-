class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        maxContainer=0
        while i<j:
            current=(j-i)*min(height[i],height[j])
            maxContainer=max(maxContainer,current)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxContainer
        