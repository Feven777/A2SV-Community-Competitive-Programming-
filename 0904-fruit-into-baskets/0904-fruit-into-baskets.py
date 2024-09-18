class Solution(object):
    def totalFruit(self, fruits):
        l=0
        max_fruit=0
        basket={}
        for r in range(len(fruits)):
            basket[fruits[r]]= basket.get(fruits[r],0)+1
            while len(basket) >2:
                basket[fruits[l]]-=1
                if basket[fruits[l]]==0:
                   del basket[fruits[l]]
                l+=1
            max_fruit=max(max_fruit,r-l+1)
        return max_fruit
            
        