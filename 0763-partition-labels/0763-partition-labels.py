class Solution(object):
    def partitionLabels(self, s):
        i=0
        ans=[]
        occur={c: i for i , c in enumerate(s)}
        mx=0
        for j in range(len(s)):
            mx=max(occur[s[j]], mx)
            if j == mx:
                ans.append((j-i)+1)
                i=j+1
   
        return ans