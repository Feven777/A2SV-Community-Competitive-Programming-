class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        j=1
        while j< len(nums):
            if nums[j]==nums[j-1]:
                j+=1
            else:
                nums[i]=nums[j]
                i+=1
                j+=1
        return i
            
            
        