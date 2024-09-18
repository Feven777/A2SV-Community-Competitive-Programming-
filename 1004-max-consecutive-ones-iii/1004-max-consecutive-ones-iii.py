class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        maxLength=0
        zeroCount=0
        for r in range (len(nums)):
            if nums[r]==0:
                zeroCount+=1
            while zeroCount>k:
                if nums[l]==0:
                    zeroCount-=1
                l+=1
            maxLength=max(maxLength,r-l+1)
        return maxLength
        