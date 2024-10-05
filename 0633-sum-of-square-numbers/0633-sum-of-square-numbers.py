class Solution(object):
    def judgeSquareSum(self, c):
        i,j=0, int(sqrt(c))
        while i<=j:
            if i**2 + j**2 == c:
                return True
            elif(i**2 +j**2 >c):
                j-=1
            else:
                i+=1
        return False
        