class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        res=0
        mod=(10**9+7)
        r=len(nums)-1
        for i, l in enumerate(nums):
            while (l+ nums[r])> target and i <= r:
                r-=1
            if i<=r:
                res += 2**(r-i)
                res%=mod
        return res
        