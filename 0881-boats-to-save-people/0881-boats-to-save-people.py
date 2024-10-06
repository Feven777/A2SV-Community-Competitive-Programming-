class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        res=0
        l,r=0, len(people)-1
        while l<=r:
            remain= limit- people[r]
            r-=1
            res+=1
            if l<=r and remain>=people[l]:
                l+=1
        return res