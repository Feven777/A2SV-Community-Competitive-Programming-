class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_names={}
        for h,n in zip(heights,names):
            height_to_names[h]=n
        res=[]
        for h in reversed(sorted(heights)):
            res.append(height_to_names[h])
        return res
            
            
                    
        