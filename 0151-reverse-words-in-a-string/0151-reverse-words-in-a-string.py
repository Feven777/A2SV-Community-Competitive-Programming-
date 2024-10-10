class Solution(object):
    def reverseWords(self, s):
        l=0
        res=""
        while l<len(s):
            while l< len(s) and s[l]== " ":
                l+=1
            if  l>=len(s): break
            r=l+1
            while r<len(s) and s[r] !=" ":
                r+=1
            w=s[l:r]
            if len(res)==0:
                res=w
            else: res=w + " " + res
            l=r+1
        return res