class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        totalSum=0
        for i in skill:
            totalSum+=i
        totalSkill=totalSum/(len(skill)/2)
        i=0
        j=len(skill)-1
        chemistry=0
        while i < j:
            if skill[i] + skill[j] == totalSkill:
                chemistry+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return chemistry
        