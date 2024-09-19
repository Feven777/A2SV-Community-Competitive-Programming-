class Solution(object):
    def numberOfSubstrings(self, s):
        l=0
        char_count={'a':0,'b':0,'c':0}
        count=0
        for r in range(len(s)):
            char_count[s[r]]+=1
            while all(char_count[char]>0 for char in 'abc'):
                count+=len(s)-r
                char_count[s[l]]-=1
                l+=1
        return count
        
        