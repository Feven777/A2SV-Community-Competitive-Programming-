class Solution(object):
    def largestNumber(self, nums):
        nums=list=(map(str,nums)) 
        def compare(a,b):
            if a+b > b+a:
                return True
            else:
                return False
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if not compare(nums[j], nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        result=''.join(nums)
        return '0' if result[0]=='0'  else result